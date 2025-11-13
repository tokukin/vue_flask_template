# run.py
from app import create_app

# 创建应用实例
app = create_app()

if __name__ == "__main__":
    # 启动应用（配置从config.py读取，默认DEBUG=True）
    app.run()  # 也可通过命令行：flask run --host=0.0.0.0 --port=8080