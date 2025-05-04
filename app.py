from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class RepairRequest(BaseModel):
    claimNo: str
    zip: str

# Mocked list of repair shops
repair_shops_db = [
    {
    "name": "Anytime Auto Glass",
    "address": "1560 River St, Boston, MA 02136",
    "phone": "617-898-8463"
  },
  {
    "name": "Safelite AutoGlass",
    "address": "1783 Revere Beach Pkwy, Everett, MA 02149",
    "phone": "800-800-2727"
  },
  {
    "name": "Local Auto Glass",
    "address": "133 S Walnut St, Quincy, MA 02169",
    "phone": "617-479-1114"
  },
{
    "name": "Allstate Auto Glass",
    "address": "519 E 5th Street, Boston, MA 02127",
    "phone": "617-770-3344"
  },
  {
    "name": "Auto Glass Now",
    "address": "139 Freeport St, Boston, MA 02122",
    "phone": "843-900-7216"
  },
  {
    "name": "AutoGlass All Boston",
    "address": "Boston, MA",
    "phone": "857-293-9155"
  }
]

@app.post("/get-repair-shops")
async def get_repair_shops(request: RepairRequest):
    return {"claimNo": request.claimNo, "zip": request.zip, "repairShops": repair_shops_db}
