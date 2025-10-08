from fastapi import HTTPException

from fastapi import APIRouter, status
from sqlalchemy.orm import Session
from fastapi import Depends

from db.session import get_db
from schemas.blog import ShowBlog, CreateBlog
from db.repository.blog import create_new_blog, retrive_blog, retrive_blog_list

router = APIRouter()

@router.post("/blogs", response_model=ShowBlog, status_code=status.HTTP_201_CREATED)
async def create_blog(blog: CreateBlog, db: Session=Depends(get_db)):
    blog = create_new_blog(blog, db, author_id=1)
    return blog


@router.get("/blogs/{id}", response_model=ShowBlog, status_code=status.HTTP_200_OK)
async def get_blog(id: int, db: Session = Depends(get_db)):
    blog = retrive_blog(id=id, db=db)
    if not blog:
        raise HTTPException(detail=f"{id} not found", status_code=status.HTTP_404_NOT_FOUND)
    return blog


@router.get("/blogs", response_model=list[ShowBlog])
async def get_all_blogs(db: Session = Depends(get_db)):
    blog_list = retrive_blog_list(db=db)
    return blog_list