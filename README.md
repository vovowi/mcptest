# MCPTest 项目

这是一个测试项目，用于展示基本的项目结构和功能。

## 项目简介

MCPTest是一个简单的演示项目，包含以下功能：

- 基本的Web API接口
- 简单的数据模型
- 单元测试示例
- 文档说明

## 技术栈

- 后端：Python + Flask
- 数据库：SQLite（开发环境）
- 测试：pytest

## 如何开始

### 环境要求

- Python 3.8+
- pip

### 安装步骤

1. 克隆仓库
```bash
git clone https://github.com/vovowi/mcptest.git
cd mcptest
```

2. 创建虚拟环境
```bash
python -m venv venv
source venv/bin/activate  # 在Windows上使用: venv\Scripts\activate
```

3. 安装依赖
```bash
pip install -r requirements.txt
```

4. 运行应用
```bash
python app.py
```

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

## 贡献指南

1. Fork 本仓库
2. 创建您的特性分支 (`git checkout -b feature/amazing-feature`)
3. 提交您的更改 (`git commit -m 'Add some amazing feature'`)
4. 推送到分支 (`git push origin feature/amazing-feature`)
5. 打开一个 Pull Request

## 许可证

本项目采用 MIT 许可证 - 详情请参阅 [LICENSE](LICENSE) 文件