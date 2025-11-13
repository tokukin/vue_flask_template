# config.py
class Config:
    DEBUG = True  # 开发环境开启调试模式
    CORS_SUPPORTS_CREDENTIALS = True  # 允许跨域携带Cookie（可选）
    # 其他配置：如数据库URI、密钥等
    # SQLALCHEMY_DATABASE_URI = "mysql+pymysql://user:password@host/dbname"