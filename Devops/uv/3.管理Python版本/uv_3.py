# uv可以安装和管理Python，并为不同项目指定不同的Python版本

# 1.查看Python版本
## 查看本机已安装以及uv可以安装的Python版本
## uv python list
## 该命令会
##     显示Python版本
##     显示Python解释器的安装路径
##     显示当前版本是否已经安装

## 查看当前项目会使用的Python解释器
## uv python find

## 查看当前项目实际运行的Python版本
## uv run python --version

## 查看当前项目实际使用的Python解释器路径
## uv run python -c "import sys; print(sys.executable)"


# 2.安装Python
## uv python install Python版本
## 例如 uv python install 3.12
## 该命令会
##     下载指定版本的Python
##     把Python安装到uv管理的目录中
##     不会自动修改当前项目使用的Python版本


# 3.固定项目使用的Python版本
## uv python pin Python版本
## 例如 uv python pin 3.12
## 该命令会
##     在项目根目录创建或修改 .python-version 文件
##     让uv优先为当前项目选择Python 3.12

## .python-version 中的 3.12 表示使用最新的Python 3.12补丁版本
## 例如实际运行的版本可能是 3.12.13


# 4.理解项目中的Python版本配置
## .python-version
##     指定当前项目本地开发时优先使用的Python版本

## pyproject.toml 中的 requires-python
##     声明该项目允许使用的Python版本范围
##     例如 requires-python = ">=3.12" 表示Python版本不能低于3.12

## .venv
##     保存当前项目实际使用的Python解释器和项目依赖

## .python-version 与 requires-python 必须兼容
## 例如 requires-python = ">=3.12" 时，不能把项目固定为Python 3.11


# 5.切换项目的Python版本
## 例如把项目从Python 3.12切换到Python 3.13
## 1.uv python install 3.13     安装Python 3.13
## 2.uv python pin 3.13         把项目固定为Python 3.13
## 3.uv sync                    根据新版本重新同步虚拟环境和依赖
## 4.uv run python --version    查看实际运行版本

## uv发现现有.venv的Python版本不符合项目设置时，会重新创建虚拟环境


