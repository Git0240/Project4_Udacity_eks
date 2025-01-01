import os

class Config:
    # Biến môi trường cho Flask
    SECRET_KEY = os.getenv('JWT_SECRET', 'default_secret_key')  # Sử dụng JWT_SECRET hoặc giá trị mặc định
    DEBUG = os.getenv('FLASK_DEBUG', True)  # Bật chế độ debug nếu cần (True/False)

    # Cấu hình SQLAlchemy cho PostgreSQL
    SQLALCHEMY_DATABASE_URI = os.getenv(
        'DATABASE_URL',
        'postgresql://postgres:0240@localhost/project4'
    )  # Thay thế 'username', 'password', 'localhost', 'db_name' bằng thông tin thực tế
    SQLALCHEMY_TRACK_MODIFICATIONS = False  # Tắt cảnh báo SQLAlchemy

    # Cấu hình môi trường
    ENV = os.getenv('FLASK_ENV', 'development')  # development, production, testing
