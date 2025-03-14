import os
from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_cors import CORS
from config import config

# 创建扩展实例
db = SQLAlchemy()
migrate = Migrate()

def create_app(config_name=None):
    """
    应用工厂函数，用于创建Flask应用实例
    """
    if config_name is None:
        config_name = os.environ.get('FLASK_CONFIG', 'default')
    
    app = Flask(__name__)
    app.config.from_object(config[config_name])
    config[config_name].init_app(app)
    
    # 初始化扩展
    db.init_app(app)
    migrate.init_app(app, db)
    CORS(app)
    
    # 注册蓝图
    from api.main import main as main_blueprint
    app.register_blueprint(main_blueprint, url_prefix='/api')
    
    # 错误处理
    @app.errorhandler(404)
    def page_not_found(e):
        return jsonify({"error": "资源不存在"}), 404
    
    @app.errorhandler(500)
    def internal_server_error(e):
        return jsonify({"error": "服务器内部错误"}), 500
    
    return app

# 创建应用实例
app = create_app()

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)