# uv可以临时运行Python工具和依赖，不需要把它们添加到当前项目中

# 1.使用uvx临时运行工具
## uvx 工具名 工具参数
## 例如 uvx ruff check .
## uvx是 uv tool run 的简写，下面两个命令作用相同
## uvx ruff check .
## uv tool run ruff check .

## 该命令会
##     为工具创建独立的临时环境
##     下载并运行工具
##     重复运行时复用uv缓存
##     不会把工具写入当前项目的 pyproject.toml 和 uv.lock

## 临时运行指定版本的工具
## 例如 uvx ruff@0.14.0 check .


# 2.临时增加依赖后运行命令
## uv run --with 依赖名 命令
## 例如 uv run --with rich python script.py
## 该命令会
##     临时提供rich依赖并运行script.py
##     不会把rich添加到当前项目依赖中

## 使用多个临时依赖
## uv run --with rich --with requests python script.py

## 在完全独立的环境中运行
## uv run --isolated --with rich python script.py


# 3.为单文件脚本声明依赖
## uv支持PEP 723格式，可以直接在Python脚本顶部声明Python版本和依赖
## 单文件脚本顶部格式如下
## # /// script
## # requires-python = ">=3.12"
## # dependencies = [
## #     "rich",
## # ]
## # ///

## 运行带依赖声明的脚本
## uv run script.py
## uv会读取脚本中的依赖声明，并创建独立环境运行脚本

## 通过命令给脚本添加依赖声明
## uv add --script script.py rich
## 该命令只修改script.py中的依赖声明，不修改项目的pyproject.toml


# 4.长期安装命令行工具
## 如果一个工具需要经常使用，可以把它安装到全局工具环境
## uv tool install ruff

## 查看已经安装的工具
## uv tool list

## 升级工具
## uv tool upgrade ruff

## 删除工具
## uv tool uninstall ruff


# 5.三种运行方式的区别
## uv run ruff
##     运行当前项目开发依赖中锁定版本的Ruff，适合项目固定使用

## uvx ruff
##     临时运行Ruff，不修改项目依赖，适合偶尔使用

## uv tool install ruff
##     把Ruff作为全局命令行工具安装，适合长期频繁使用


# 6.常用的临时运行步骤
## 1.uvx ruff check .                       临时运行代码检查工具
## 2.uv run --with rich python script.py    临时增加依赖并运行脚本
## 3.uv add --script script.py rich         给单文件脚本声明依赖
## 4.uv run script.py                       自动安装脚本依赖并运行
