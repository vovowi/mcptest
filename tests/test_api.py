import unittest
import json
from app import create_app, db
from models.user import User

class APITestCase(unittest.TestCase):
    """API测试用例"""
    
    def setUp(self):
        """测试前准备"""
        self.app = create_app('testing')
        self.app_context = self.app.app_context()
        self.app_context.push()
        db.create_all()
        self.client = self.app.test_client()
        
        # 创建测试用户
        self.user = User(username='test', email='test@example.com')
        self.user.set_password('password')
        db.session.add(self.user)
        db.session.commit()
    
    def tearDown(self):
        """测试后清理"""
        db.session.remove()
        db.drop_all()
        self.app_context.pop()
    
    def test_index(self):
        """测试API根路径"""
        response = self.client.get('/api/')
        self.assertEqual(response.status_code, 200)
        json_response = json.loads(response.get_data(as_text=True))
        self.assertEqual(json_response['status'], 'success')
        self.assertEqual(json_response['message'], '欢迎使用MCPTest API')
    
    def test_get_users(self):
        """测试获取用户列表"""
        response = self.client.get('/api/users')
        self.assertEqual(response.status_code, 200)
        json_response = json.loads(response.get_data(as_text=True))
        self.assertEqual(json_response['status'], 'success')
        self.assertEqual(len(json_response['users']), 1)
        self.assertEqual(json_response['users'][0]['username'], 'test')
    
    def test_get_user(self):
        """测试获取单个用户"""
        response = self.client.get(f'/api/users/{self.user.id}')
        self.assertEqual(response.status_code, 200)
        json_response = json.loads(response.get_data(as_text=True))
        self.assertEqual(json_response['status'], 'success')
        self.assertEqual(json_response['user']['username'], 'test')
        self.assertEqual(json_response['user']['email'], 'test@example.com')
    
    def test_create_user(self):
        """测试创建用户"""
        response = self.client.post(
            '/api/users',
            data=json.dumps({
                'username': 'new_user',
                'email': 'new_user@example.com',
                'password': 'password'
            }),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, 201)
        json_response = json.loads(response.get_data(as_text=True))
        self.assertEqual(json_response['status'], 'success')
        self.assertEqual(json_response['user']['username'], 'new_user')
        self.assertEqual(json_response['user']['email'], 'new_user@example.com')
        
        # 验证用户已添加到数据库
        user = User.query.filter_by(username='new_user').first()
        self.assertIsNotNone(user)
        self.assertEqual(user.email, 'new_user@example.com')
    
    def test_update_user(self):
        """测试更新用户"""
        response = self.client.put(
            f'/api/users/{self.user.id}',
            data=json.dumps({
                'email': 'updated@example.com'
            }),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, 200)
        json_response = json.loads(response.get_data(as_text=True))
        self.assertEqual(json_response['status'], 'success')
        self.assertEqual(json_response['user']['email'], 'updated@example.com')
        
        # 验证用户已更新
        user = User.query.get(self.user.id)
        self.assertEqual(user.email, 'updated@example.com')
    
    def test_delete_user(self):
        """测试删除用户"""
        response = self.client.delete(f'/api/users/{self.user.id}')
        self.assertEqual(response.status_code, 200)
        json_response = json.loads(response.get_data(as_text=True))
        self.assertEqual(json_response['status'], 'success')
        
        # 验证用户已删除
        user = User.query.get(self.user.id)
        self.assertIsNone(user)