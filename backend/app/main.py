import os
from typing import List
from uuid import UUID
from fastapi import Depends, FastAPI, HTTPException, status
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session
from .db import Base, engine, get_db
from .models import Asset
from .schemas import AssetCreate, AssetRead
Base.metadata.create_all(bind=engine)
app=FastAPI(title='DHG Core Asset Service',version='0.1.0')
origins=['http://localhost:5173','http://127.0.0.1:5173']
app.add_middleware(CORSMiddleware,allow_origins=origins,allow_credentials=True,allow_methods=['*'],allow_headers=['*'])
@app.get('/health')
def health(): return {'status':'ok'}
@app.get('/assets',response_model=List[AssetRead])
def list_assets(db:Session=Depends(get_db)):return db.query(Asset).all()
@app.post('/assets',response_model=AssetRead,status_code=201)
def create_asset(payload:AssetCreate,db:Session=Depends(get_db)):
    a=Asset(title=payload.title,description=payload.description,kind=payload.kind)
    db.add(a); db.commit(); db.refresh(a); return a
@app.get('/assets/{asset_id}',response_model=AssetRead)
def get_asset(asset_id:UUID,db:Session=Depends(get_db)):
    a=db.query(Asset).filter(Asset.id==asset_id).first()
    if not a: raise HTTPException(404,'Asset not found')
    return a