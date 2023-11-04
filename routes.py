from fastapi import APIRouter, Body, Request, Response, HTTPException, status
from fastapi.encoders import jsonable_encoder
from typing import List

from models import Food, History, FoodWithHistory

router = APIRouter()


@router.get("/", response_description="Get all foods", response_model=List[Food])
def get_foods(request: Request):
    return request.app.database["foods"].find()


@router.get("/{food_id}", response_description="Get a certain food", response_model=Food)
def get_food(request: Request, food_id: str):
    item = request.app.database["foods"].find_one({"food_id": food_id})
    print(item)
    if item is not None:
        return item
    raise HTTPException(status_code=404)


@router.get("/history/all", response_description="Get history", response_model=List[History])
def get_all_history(request: Request):
    items = request.app.database["history"].find().limit(20)
    print(items)
    if items is not None:
        return items
    raise HTTPException(status_code=404)


@router.get("/history/{food}", response_description="get food's history", response_model=FoodWithHistory)
def get_food_history(request: Request, food: str):
    result = request.app.database['foods'].aggregate([
        {
            '$match': {
                'food_id': food
            }
        }, {
            '$lookup': {
                'from': 'history',
                'localField': '_id',
                'foreignField': 'food_id',
                'as': 'prices'
            }
        }
    ])
    print(result)
    if result is not None:
        return list(result)[0]
    raise HTTPException(status_code=404)
