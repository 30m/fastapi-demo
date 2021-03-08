from typing import List
from fastapi import APIRouter

routor = APIRouter()


@routor.get("/")
async def get_all_hedgehogs() -> List[dict]:
  hedgehogs = [
      {"id": 1, "name": "momo", "color": "SALT & PEPPER", "age": 2},
      {"id": 2, "name": "coco", "color": "DARK GRAY", "age": 1.5}
  ]
  return hedgehogs
