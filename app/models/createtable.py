"""
用于生成表
需要手动创建数据库

"""
import main
from app.models.model import db
db.create_all()