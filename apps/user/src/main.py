from typing import Annotated
from fastapi import FastAPI, Depends, HTTPException
from fastapi.concurrency import asynccontextmanager
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.ext.declarative import declarative_base
from src.database import get_db_session, sessionmanager
from src.schemas.user_schema import UserCreate
import src.user.user_service as crud

import src.models

@asynccontextmanager
async def lifespan(app: FastAPI):
    """
    Function that handles startup and shutdown events.
    To understand more, read https://fastapi.tiangolo.com/advanced/events/
    """
    yield
    if sessionmanager._engine is not None:
        # Close the DB connection
        await sessionmanager.close()

app = FastAPI(lifespan=lifespan)


@app.post("/documents/", response_model=DocumentBase)
async def create_document(document_data: DocumentCreate, db: AsyncSession = Depends(get_db_session)):
    return await document_crud.create(db, document_data)

@app.get("/documents/", response_model=List[DocumentBase])
async def get_all_documents(db: AsyncSession = Depends(get_db_session)):
    return await document_crud.get_all(db)

@app.get("/documents/{document_id}", response_model=DocumentBase)
async def get_document(document_id: int, db: AsyncSession = Depends(get_db_session)):
    document = await document_crud.get(db, document_id)
    if document is None:
        raise HTTPException(status_code=404, detail="Document not found")
    return document

@app.put("/documents/{document_id}", response_model=DocumentBase)
async def update_document(document_id: int, update_data: DocumentCreate, db: AsyncSession = Depends(get_db_session)):
    return await document_crud.update(db, document_id, update_data)

@app.delete("/documents/{document_id}")
async def delete_document(document_id: int, db: AsyncSession = Depends(get_db_session)):
    await document_crud.delete(db, document_id)
    return {"message": "Document deleted successfully"} 
