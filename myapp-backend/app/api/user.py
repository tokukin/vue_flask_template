# app/api/user.py
from flask import Blueprint, jsonify, request
# 若有复杂逻辑，可导入服务层（如用户数据查询）
from app.services.user_service import get_user_info

# 1. 创建蓝图实例（参数：蓝图名、模块名、url_prefix可在注册时统一配置）
user_bp = Blueprint("user", __name__)

# 2. 定义该模块的路由（路径会自动拼接注册时的前缀 /api/user）
@user_bp.route("/info", methods=["GET"])
def get_user():
    """获取用户信息接口：/api/user/info"""
    user_id = request.args.get("user_id")  # 从请求参数获取user_id
    if not user_id:
        return jsonify({"code": 400, "message": "缺少user_id参数"}), 400
    
    # 调用服务层逻辑（抽离复杂代码，保持视图函数简洁）
    user_data = get_user_info(user_id)
    if not user_data:
        return jsonify({"code": 404, "message": "用户不存在"}), 404
    
    return jsonify({"code": 200, "data": user_data})

@user_bp.route("/login", methods=["POST"])
def user_login():
    """用户登录接口：/api/user/login"""
    login_data = request.get_json()  # 获取POST请求的JSON数据
    username = login_data.get("username")
    password = login_data.get("password")
    
    # 模拟登录校验（实际项目需对接数据库+加密校验）
    if username == "admin" and password == "123456":
        return jsonify({"code": 200, "message": "登录成功", "data": {"token": "fake-token-123"}})
    else:
        return jsonify({"code": 401, "message": "用户名或密码错误"}), 401