import unittest
from app import create_app, db
from models.user import User

class UserModelTestCase(unittest.TestCase):
    """用户模型测试用例"""
    
    def setUp(self):
        """测试前准备"""
        self.app = create_app('testing')
        self.app_context = self.app.app_context()
        self.app_context.push()
        db.create_all()
    
    def tearDown(self):
        """测试后清理"""
        db.session.remove()
        db.drop_all()
        self.app_context.pop()
    
    def test_password_setter(self):
        """测试密码设置"""
        u = User(username='test', email='test@example.com')
        u.set_password('cat')
        self.assertTrue(u.password_hash is not None)
    
    def test_no_password_getter(self):
        """测试密码不可读"""
        u = User(username='test', email='test@example.com')
        u.set_password('cat')
        with self.assertRaises(AttributeError):
            u.password
    
    def test_password_verification(self):
        """测试密码验证"""
        u = User(username='test', email='test@example.com')
        u.set_password('cat')
        self.assertTrue(u.verify_password('cat'))
        self.assertFalse(u.verify_password('dog'))
    
    def test_password_salts_are_random(self):
        """测试密码盐值随机"""
        u1 = User(username='test1', email='test1@example.com')
        u1.set_password('cat')
        u2 = User(username='test2', email='test2@example.com')
        u2.set_password('cat')
        self.assertNotEqual(u1.password_hash, u2.password_hash)
    
    def test_to_json(self):
        """测试JSON序列化"""
        u = User(username='test', email='test@example.com')
        db.session.add(u)
        db.session.commit()
        json_user = u.to_json()
        self.assertEqual(json_user['username'], 'test')
        self.assertEqual(json_user['email'], 'test@example.com')
        self.assertTrue('created_at' in json_user)
        self.assertTrue('updated_at' in json_user)
        self.assertTrue('id' in json_user)
        self.assertFalse('password_hash' in json_user)