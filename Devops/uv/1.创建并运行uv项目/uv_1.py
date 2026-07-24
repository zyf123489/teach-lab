# uv是一个用Rust编写的Python项目和依赖管理工具

# 1. 安装uv
## 首先要进入到项目的根目录，打开命令行，通过 pip install uv 来安装uv
## 安装成功后便可看到uv的版本号
## 通过 uv --version 来查看uv的版本号
## 通过 uv init 命令来进行uv项目的初始化
## 初始化成功后便可看到根目录下产生了许多新文件
## .python-version   这个项目使用的 Python 版本
## main.py           项目入口文件
## pyproject.toml    项目名称、Python 版本和依赖配置
## README.md         项目说明

# 2. 运行uv
## 进入到项目的根目录，打开命令行，通过 uv run 命令来运行项目
## 例如 uv run main.py
## 运行成功后便可看到控制台输出 Hello from uv!
## 运行uv run / uv sync /uv add 时就会自动创建两个新文件
## .venv            虚拟环境目录
## uv.lock          精确依赖锁文件（保证所有人安装一样的版本）
## 通常第一次运行uv时，还需要：
##      选择Python版本
##      创建虚拟环境（.venv）
##      同步依赖
##      在虚拟环境中运行项目


# 一般自己从0写项目uv的使用步骤
## 1.pip install uv                 全局安装 uv 工具
## 2.uv init                        初始化项目
## 3.uv python pin 3.12             锁定本项目使用的 Python 版本为 3.12
## 5.uv add requests                添加正式业务依赖
## 6.uv add --dev pytest ruff mypy  添加开发依赖（仅本地开发用，打包发布不会带上）
## 7.uv run main.py                 使用本地 .venv 里面的 Python 运行脚本


# 自己克隆别人的项目
## 项目里必须存在这两个文件
## pyproject.toml + uv.lock
## 如果本地有.venv 文件，则需要先删除
## 1.uv sync    读取uv.lock 文件，安装依赖
## 2.uv run main.py  运行项目