from typing import List, Optional

from fastapi import FastAPI, Query

from modules.reasoner import Reasoner

app = FastAPI()
reasoner = Reasoner()


@app.get("/recommendations")
def get_recommendations_by_product_name(title: str, filters: Optional[List[str]] = Query(None), limit: int = 20):
    result = reasoner.get_recommendations(title, filters, limit)
    return {"recommendations": result}