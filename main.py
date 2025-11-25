from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from configs.db_connection import Base, engine, SessionLocal
from models.Collar import Collar
from utils import build_tag  

Base.metadata.create_all(bind=engine)

app = FastAPI()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.post("/collars")
def criar_collar(pet_id: int | None = None, db: Session = Depends(get_db)):
    tag = build_tag()

    while db.query(Collar).filter(Collar.tag == tag).first():
        tag = build_tag()

    new_collar = Collar(
        pet_id=pet_id,
        tag=tag,
        status=False,
        available_balance=0
    )

    db.add(new_collar)
    db.commit()
    db.refresh(new_collar)

    return {
        "id": new_collar.id,
        "tag": new_collar.tag,
        "pet_id": new_collar.pet_id,
        "status": new_collar.status,
        "available_balance": float(new_collar.available_balance or 0)
    }


import uvicorn

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)