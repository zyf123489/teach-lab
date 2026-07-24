# 项目依赖就是需要使用到的Python第三方库

# 1.添加依赖
## uv add 依赖名
## 例如 uv add requests
## 该命令会
##     依赖声明写入 pyproject.toml
##     把精确版本和间接依赖写入 uv.lock
##     把依赖安装到 .venv

# 2.查看依赖
## 查看所有依赖
## uv tree
## 该命令会
##     打印所有依赖的精确版本
##     打印所有依赖的间接依赖
##     打印所有依赖的依赖树

## 平铺列出所有已安装包清单
## uv pip list
## 该命令会
##     打印所有已安装包的精确版本

## 查看单个包详情
## uv pip show 包名
## 该命令会
##     打印单个包的精确版本
##     打印单个包的依赖树


# 3.删除依赖
## uv remove 依赖名
## 例如 uv remove requests
## 该命令会
##     依赖声明从 pyproject.toml 中移除
##     把依赖从 .venv 中移除

# 4.同步依赖
## uv sync
## 该命令会
##     读取 uv.lock 文件
##     安装依赖到 .venv

# 5.升级依赖
## uv upgrade 依赖名
## 例如 uv upgrade requests
## 该命令会
##     升级依赖的精确版本
##     把依赖安装到 .venv
