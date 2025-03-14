from flask import jsonify, request
from . import main
from app import db
from models.user import User

@main.route('/', methods=['GET'])
def index():
    """API根路径"""
    return jsonify({
        'message': '欢迎使用MCPTest API',
        'status': 'success',
        'version': '1.0.0'
    })

@main.route('/users', methods=['GET'])
def get_users():
    """获取所有用户"""
    users = User.query.all()
    return jsonify({
        'status': 'success',
        'users': [user.to_json() for user in users]
    })

@main.route('/users/<int:id>', methods=['GET'])
def get_user(id):
    """获取指定ID的用户"""
    user = User.query.get_or_404(id)
    return jsonify({
        'status': 'success',
        'user': user.to_json()
    })

@main.route('/users', methods=['POST'])
def create_user():
    """创建新用户"""
    data = request.get_json()
    if not data:
        return jsonify({'status': 'error', 'message': '无效的数据'}), 400
    
    # 数据验证
    if not data.get('username') or not data.get('email'):
        return jsonify({'status': 'error', 'message': '用户名和邮箱不能为空'}), 400
    
    # 检查用户名和邮箱是否已存在
    if User.query.filter_by(username=data.get('username')).first():
        return jsonify({'status': 'error', 'message': '用户名已存在'}), 400
    
    if User.query.filter_by(email=data.get('email')).first():
        return jsonify({'status': 'error', 'message': '邮箱已存在'}), 400
    
    # 创建新用户
    user = User(
        username=data.get('username'),
        email=data.get('email')
    )
    
    # 如果提供了密码，则设置密码
    if data.get('password'):
        user.set_password(data.get('password'))
    
    # 保存到数据库
    try:
        db.session.add(user)
        db.session.commit()
        return jsonify({
            'status': 'success',
            'message': '用户创建成功',
            'user': user.to_json()
        }), 201
    except Exception as e:
        db.session.rollback()
        return jsonify({'status': 'error', 'message': f'创建用户失败: {str(e)}'}), 500

@main.route('/users/<int:id>', methods=['PUT'])
def update_user(id):
    """更新用户信息"""
    user = User.query.get_or_404(id)
    data = request.get_json()
    
    if not data:
        return jsonify({'status': 'error', 'message': '无效的数据'}), 400
    
    # 更新用户信息
    if data.get('username'):
        # 检查新用户名是否已存在
        existing_user = User.query.filter_by(username=data.get('username')).first()
        if existing_user and existing_user.id != id:
            return jsonify({'status': 'error', 'message': '用户名已存在'}), 400
        user.username = data.get('username')
    
    if data.get('email'):
        # 检查新邮箱是否已存在
        existing_user = User.query.filter_by(email=data.get('email')).first()
        if existing_user and existing_user.id != id:
            return jsonify({'status': 'error', 'message': '邮箱已存在'}), 400
        user.email = data.get('email')
    
    # 如果提供了新密码，则更新密码
    if data.get('password'):
        user.set_password(data.get('password'))
    
    # 保存到数据库
    try:
        db.session.commit()
        return jsonify({
            'status': 'success',
            'message': '用户更新成功',
            'user': user.to_json()
        })
    except Exception as e:
        db.session.rollback()
        return jsonify({'status': 'error', 'message': f'更新用户失败: {str(e)}'}), 500

@main.route('/users/<int:id>', methods=['DELETE'])
def delete_user(id):
    """删除用户"""
    user = User.query.get_or_404(id)
    
    try:
        db.session.delete(user)
        db.session.commit()
        return jsonify({
            'status': 'success',
            'message': '用户删除成功'
        })
    except Exception as e:
        db.session.rollback()
        return jsonify({'status': 'error', 'message': f'删除用户失败: {str(e)}'}), 500