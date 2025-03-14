# 安装指南

## 环境要求

- Python 3.8+
- pip

## 安装步骤

### 1. 克隆仓库

```bash
git clone https://github.com/vovowi/mcptest.git
cd mcptest
```

### 2. 创建虚拟环境

在Windows上:

```bash
python -m venv venv
venv\Scripts\activate
```

在macOS/Linux上:

```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. 安装依赖

```bash
pip install -r requirements.txt
```

### 4. 配置环境变量

创建一个`.env`文件在项目根目录:

```
FLASK_APP=app.py
FLASK_CONFIG=development
SECRET_KEY=your-secret-key
```

### 5. 初始化数据库

```bash
flask db init
flask db migrate -m "initial migration"
flask db upgrade
```

### 6. 运行应用

```bash
flask run
```

或者直接运行:

```bash
python app.py
```

应用将在 http://127.0.0.1:5000 上运行。

## 部署到生产环境

### 使用Gunicorn (Linux/macOS)

```bash
pip install gunicorn
gunicorn -w 4 -b 0.0.0.0:8000 app:app
```

### 使用Docker

1. 构建Docker镜像:

```bash
docker build -t mcptest .
```

2. 运行容器:

```bash
docker run -d -p 8000:5000 mcptest
```

## 常见问题

### 数据库迁移错误

如果遇到数据库迁移错误，尝试删除`migrations`文件夹并重新初始化:

```bash
rm -rf migrations
flask db init
flask db migrate -m "initial migration"
flask db upgrade
```

### 依赖安装问题

如果安装依赖时遇到问题，尝试更新pip:

```bash
pip install --upgrade pip
```

然后重新安装依赖:

```bash
pip install -r requirements.txt
```