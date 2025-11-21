from fastapi import FastAPI

app = FastAPI()

# Sample in-memory database
items = []

@app.get("/items")
def read_items():
    return items

@app.post("/items")
def create_item(item: dict):
    items.append(item)
    return {"message": "Item added successfully", "item": item}

@app.put("/items/{item_id}")
def update_item(item_id: int, updated_item: dict):
    if 0 <= item_id < len(items):
        items[item_id] = updated_item
        return {"message": "Item updated successfully", "item": updated_item}
    return {"error": "Item not found"}

@app.delete("/items/{item_id}")
def delete_item(item_id: int):
    if 0 <= item_id < len(items):
        removed_item = items.pop(item_id)
        return {"message": "Item deleted successfully", "item": removed_item}
    return {"error": "Item not found"}