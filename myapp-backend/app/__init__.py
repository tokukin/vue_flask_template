# app/__init__.py
from flask import Flask
from flask_cors import CORS
from config import Config
# 导入各模块的蓝图
from app.api.user import user_bp


def create_app(config_class=Config):
    # 1. 创建Flask应用实例
    app = Flask(__name__)
    # 2. 加载配置
    app.config.from_object(config_class)
    # 3. 配置CORS（允许所有域，生产环境可指定具体域名如origins="https://your-frontend.com"）
    CORS(app, resources={r"/api/*": {"origins": "*"}})
    
    # 4. 注册蓝图（所有业务模块的接口统一挂载到 /api 前缀下）
    app.register_blueprint(user_bp, url_prefix="/api/user")    # 用户接口前缀：/api/user
    
    
    return app