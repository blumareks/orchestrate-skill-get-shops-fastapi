from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class RepairRequest(BaseModel):
    claimNo: str
    zip: str

# Mocked list of repair shops
repair_shops_db = [
    {"name": "Speedy Auto Glass", "address": "123 Glass St, Pleasant Hill, CA","phone":"925-100-1234"},
    {"name": "Elite Windshield Repair", "address": "456 Auto Blvd, Oakland, CA","phone":"925-100-1000"},
    {"name": "Bay Area Glass Pros", "address": "789 Car Dr, San Francisco, CA","phone":"415-100-1000"},
    {"name": "Quick Fix Auto Glass", "address": "101 Fast Ln, San Mateo, CA","phone":"510-100-1000"},
    {"name": "Precision Windshield Experts", "address": "202 Car St, Berkeley, CA","phone":"925-100-1000"},
]

@app.post("/get-repair-shops")
async def get_repair_shops(request: RepairRequest):
    return {"claimNo": request.claimNo, "zip": request.zip, "repairShops": repair_shops_db}
