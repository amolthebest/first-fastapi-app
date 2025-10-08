from schemas.blog import CreateBlog
from sqlalchemy.orm import Session
from db.models.blogs import Blog

def create_new_blog(blog: CreateBlog, db: Session, author_id: int=1):
    blog = Blog(**blog.dict(), author_id=author_id)
    db.add(blog)
    db.commit()
    db.refresh(blog)
    return blog

def retrive_blog(id: int, db:Session):
    blog = db.query(Blog).filter(Blog.id == id).first()
    return blog

def retrive_blog_list(db: Session):
    blog_list = db.query(Blog).all()
    return blog_list