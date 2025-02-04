from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class RepairRequest(BaseModel):
    claimNo: str
    zip: str

# Mocked list of repair shops
repair_shops_db = [
    {"name": "Speedy Auto Glass", "address": "123 Glass St, Pleasant Hill, CA"},
    {"name": "Elite Windshield Repair", "address": "456 Auto Blvd, Oakland, CA"},
    {"name": "Bay Area Glass Pros", "address": "789 Car Dr, San Francisco, CA"},
    {"name": "Quick Fix Auto Glass", "address": "101 Fast Ln, San Mateo, CA"},
    {"name": "Precision Windshield Experts", "address": "202 Car St, Berkeley, CA"},
]

@app.post("/get-repair-shops")
async def get_repair_shops(request: RepairRequest):
    return {"claimNo": request.claimNo, "zip": request.zip, "repairShops": repair_shops_db}
