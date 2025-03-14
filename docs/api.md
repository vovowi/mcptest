# API 文档

## 基本信息

- 基础URL: `/api`
- 所有响应均为JSON格式
- 状态码:
  - 200: 成功
  - 201: 创建成功
  - 400: 请求错误
  - 404: 资源不存在
  - 500: 服务器错误

## 端点

### 1. 获取API信息

获取API基本信息。

- **URL**: `/`
- **方法**: `GET`
- **响应示例**:

```json
{
  "message": "欢迎使用MCPTest API",
  "status": "success",
  "version": "1.0.0"
}
```

### 2. 用户管理

#### 2.1 获取所有用户

获取所有用户的列表。

- **URL**: `/users`
- **方法**: `GET`
- **响应示例**:

```json
{
  "status": "success",
  "users": [
    {
      "id": 1,
      "username": "user1",
      "email": "user1@example.com",
      "created_at": "2025-03-14T12:00:00",
      "updated_at": "2025-03-14T12:00:00"
    },
    {
      "id": 2,
      "username": "user2",
      "email": "user2@example.com",
      "created_at": "2025-03-14T13:00:00",
      "updated_at": "2025-03-14T13:00:00"
    }
  ]
}
```

#### 2.2 获取单个用户

获取指定ID的用户信息。

- **URL**: `/users/<id>`
- **方法**: `GET`
- **URL参数**: `id` - 用户ID
- **响应示例**:

```json
{
  "status": "success",
  "user": {
    "id": 1,
    "username": "user1",
    "email": "user1@example.com",
    "created_at": "2025-03-14T12:00:00",
    "updated_at": "2025-03-14T12:00:00"
  }
}
```

#### 2.3 创建用户

创建新用户。

- **URL**: `/users`
- **方法**: `POST`
- **请求体**:

```json
{
  "username": "newuser",
  "email": "newuser@example.com",
  "password": "password123"
}
```

- **响应示例**:

```json
{
  "status": "success",
  "message": "用户创建成功",
  "user": {
    "id": 3,
    "username": "newuser",
    "email": "newuser@example.com",
    "created_at": "2025-03-14T14:00:00",
    "updated_at": "2025-03-14T14:00:00"
  }
}
```

#### 2.4 更新用户

更新指定ID的用户信息。

- **URL**: `/users/<id>`
- **方法**: `PUT`
- **URL参数**: `id` - 用户ID
- **请求体**:

```json
{
  "email": "updated@example.com"
}
```

- **响应示例**:

```json
{
  "status": "success",
  "message": "用户更新成功",
  "user": {
    "id": 1,
    "username": "user1",
    "email": "updated@example.com",
    "created_at": "2025-03-14T12:00:00",
    "updated_at": "2025-03-14T15:00:00"
  }
}
```

#### 2.5 删除用户

删除指定ID的用户。

- **URL**: `/users/<id>`
- **方法**: `DELETE`
- **URL参数**: `id` - 用户ID
- **响应示例**:

```json
{
  "status": "success",
  "message": "用户删除成功"
}
```