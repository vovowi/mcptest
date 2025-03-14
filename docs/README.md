# MCPTest 项目文档

## 简介

MCPTest是一个简单的Web API演示项目，用于展示基本的项目结构和功能。

## 目录

- [安装指南](installation.md)
- [API文档](api.md)
- [开发指南](development.md)

## 项目结构

```
mcptest/
├── app.py              # 应用入口
├── config.py           # 配置文件
├── requirements.txt    # 项目依赖
├── models/             # 数据模型
├── api/                # API接口
├── services/           # 业务逻辑
├── tests/              # 测试文件
└── docs/               # 文档
```

## 技术栈

- 后端：Python + Flask
- 数据库：SQLite（开发环境）
- 测试：pytest

## 贡献指南

请参阅[开发指南](development.md)了解如何为项目做出贡献。