# app/services/user_service.py
def get_user_info(user_id):
    """模拟从数据库获取用户信息（实际项目需对接MySQL/PostgreSQL等）"""
    # 这里用字典模拟数据库数据
    mock_users = {
        "1": {"id": "1", "username": "zhangsan", "age": 25, "email": "zhangsan@example.com","message":"Flask+Vue+Vite hello"},
        "2": {"id": "2", "username": "lisi", "age": 30, "email": "lisi@example.com","message":"Flask+Vue+Vite hello"}
    }
    return mock_users.get(user_id)  # 根据user_id返回用户数据