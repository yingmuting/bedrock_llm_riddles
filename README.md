# 完蛋！我被Bedrock LLM包围了！

## 简介
《完蛋！我被Bedrock LLM包围了！》是一款智力挑战游戏，在这个游戏中，玩家需要巧妙构造问题，挑战LLM给出满足特定条件的回答。

## 目标
1. AWS Bedrock提供托管多个主流的LLM大模型，支持通过SDK/API/CLI方式调用，方便开发者熟悉调用Bedrock服务
2. 通过关卡挑战，方便玩家了解prompt engineering的魅力

## 更新
2023.11. 发布第一版，支持AWS Bedrock Claude V2模型，通关包括m个关卡，n个问题

## 开始游戏

### 在线体验
要开始游戏，请按照以下步骤操作：

1. 前往[AWS Sagemaker Notebook](https://us-east-1.console.aws.amazon.com/sagemaker/home?region=us-east-1#/notebook-instances)，创建笔记本实例，建议使用管理员账号
2. 克隆项目代码：
   ```
   git clone https://github.com/yingmuting/bedrock_llm_riddles.git
   ```
2. 进入到`sagemaker/`目录
3. 安装所需的Python依赖`pip install -r requirements.txt`
4. 前往[AWS Bedrock](https://us-east-1.console.aws.amazon.com/bedrock/home) 打开左侧菜单“Model access”，点击“Manage model access”开通“Anthropic”-“Claude”模型访问权限
5. 执行启动命令`python app.py`

## 贡献指南
我们欢迎大家为《完蛋！我被Bedrock LLM包围了！》做出贡献，包括提出更多好玩的问题，提供更多的玩法。请按以下步骤操作：

1. 访问项目地址 [Bedrock LLMRiddles](https://github.com/yingmuting/bedrock_llm_riddles/) 并fork项目。
2. 在你的本地环境中创建你的特性分支 (`git checkout -b feature/AmazingFeature`)。
3. 提交你的改动 (`git commit -m 'Add some AmazingFeature'`)。
4. 将你的改动推送到分支上 (`git push origin feature/AmazingFeature`)。
5. 在原项目下发起一个Pull Request。

## 支持
如果你在游戏过程中遇到任何问题或需要帮助，请通过项目的[Issues页面](https://github.com/yingmuting/bedrock_llm_riddles/issues)提交你的问题。
