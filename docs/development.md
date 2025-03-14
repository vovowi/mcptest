# 开发指南

## 开发环境设置

请参阅[安装指南](installation.md)设置开发环境。

## 代码规范

本项目遵循PEP 8代码规范。建议使用以下工具来保持代码质量：

- flake8: 代码风格检查
- black: 代码格式化
- isort: 导入排序

可以通过以下命令安装这些工具：

```bash
pip install flake8 black isort
```

## 分支管理

- `main`: 主分支，保持稳定可发布状态
- `develop`: 开发分支，新功能合并到此分支
- `feature/*`: 功能分支，从`develop`分支创建
- `bugfix/*`: 修复分支，从`develop`分支创建
- `release/*`: 发布分支，从`develop`分支创建
- `hotfix/*`: 热修复分支，从`main`分支创建

## 开发流程

1. 从`develop`分支创建新的功能分支：

```bash
git checkout develop
git pull
git checkout -b feature/your-feature-name
```

2. 在功能分支上进行开发，定期提交更改：

```bash
git add .
git commit -m "描述你的更改"
```

3. 完成功能开发后，将`develop`分支合并到你的功能分支：

```bash
git checkout develop
git pull
git checkout feature/your-feature-name
git merge develop
```

4. 解决可能的冲突，然后推送你的分支：

```bash
git push origin feature/your-feature-name
```

5. 创建Pull Request，请求将你的功能分支合并到`develop`分支。

## 测试

### 运行测试

使用pytest运行测试：

```bash
pytest
```

运行特定测试文件：

```bash
pytest tests/test_user_model.py
```

运行带覆盖率报告的测试：

```bash
pytest --cov=app tests/
```

### 编写测试

- 所有测试文件应放在`tests/`目录下
- 测试文件名应以`test_`开头
- 测试类名应以`Test`开头
- 测试方法名应以`test_`开头

测试示例：

```python
def test_user_creation():
    user = User(username='test', email='test@example.com')
    assert user.username == 'test'
    assert user.email == 'test@example.com'
```

## 数据库迁移

创建新的迁移：

```bash
flask db migrate -m "描述迁移内容"
```

应用迁移：

```bash
flask db upgrade
```

回滚迁移：

```bash
flask db downgrade
```

## 文档

- API文档在`docs/api.md`中维护
- 更新代码时，请同时更新相关文档

## 提交Pull Request

1. 确保你的代码通过所有测试
2. 确保你的代码符合代码规范
3. 更新相关文档
4. 创建Pull Request，详细描述你的更改
5. 等待代码审查

## 发布流程

1. 从`develop`分支创建发布分支：

```bash
git checkout develop
git pull
git checkout -b release/vX.Y.Z
```

2. 在发布分支上进行最终测试和修复

3. 完成发布后，将发布分支合并到`main`和`develop`分支：

```bash
git checkout main
git merge release/vX.Y.Z
git tag vX.Y.Z
git push origin main --tags

git checkout develop
git merge release/vX.Y.Z
git push origin develop
```

4. 删除发布分支：

```bash
git branch -d release/vX.Y.Z
```