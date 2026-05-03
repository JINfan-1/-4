# DeepSeek 终端流式对话程序

## 项目简介
这是一个使用 Python 调用 DeepSeek API 实现的终端流式对话程序。

## 我完成的内容
- 使用 `venv` 创建虚拟环境
- 安装依赖
- 通过环境变量或 `.env` 文件读取 API Key
- 调用 DeepSeek API
- 实现终端输入输出
- 实现流式输出
- 支持退出命令（`exit`/`quit`/`q`）

## 运行方式

### 1. 创建虚拟环境
请先创建并激活 `.venv` 虚拟环境：
```bash
# 创建虚拟环境
python -m venv .venv

# Windows 激活
.venv\Scripts\activate

# macOS/Linux 激活
source .venv/bin/activate
```
### 2. 安装依赖
- 安装 requirements.txt 中的依赖：
```pip install -r requirements.txt```
### 3. 配置 API Key
- 创建 .env 文件：
```DEEPSEEK_API_KEY=你的API密钥```
### 4. 运行程序
- 运行主程序：
```python main.py```
## 实现思路
- 通过 python-dotenv 读取 .env 文件中的 API Key，使用 OpenAI 兼容的客户端调用 DeepSeek 接口，并在终端中实现了流式输出效果。程序会持续接收用户输入，直到用户输入退出命令。