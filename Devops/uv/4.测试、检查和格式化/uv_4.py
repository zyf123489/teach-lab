# 测试、检查和格式化工具通常只在开发时使用，因此应该添加为开发依赖

# 1.添加开发依赖
## uv add --dev 开发依赖名
## 例如 uv add --dev pytest ruff mypy
## 该命令会
##     把开发依赖写入 pyproject.toml 的 dev 依赖组
##     把开发依赖的精确版本写入 uv.lock
##     把开发依赖安装到 .venv

## 正式依赖与开发依赖的区别
##     正式依赖是程序运行时必须使用的依赖，例如 requests
##     开发依赖是测试和检查代码时使用的依赖，例如 pytest、ruff、mypy


# 2.使用pytest运行测试
## 运行项目中的所有测试
## uv run pytest

## 显示更详细的测试结果
## uv run pytest -v

## 运行指定测试文件
## uv run pytest tests/test_example.py

## 运行名称中包含指定内容的测试
## uv run pytest -k test_name


# 3.使用Ruff检查代码
## 检查当前项目中的Python代码
## uv run ruff check .

## 自动修复能够安全修复的问题
## uv run ruff check . --fix

## Ruff会检查
##     没有使用的导入
##     不符合规范的代码
##     常见的Python代码错误


# 4.格式化代码
## 使用项目开发依赖中的Ruff格式化代码
## uv run ruff format .

## 只检查格式，不修改文件
## uv run ruff format . --check

## 新版本uv也可以直接使用下面的命令调用Ruff格式化项目
## uv format

## 只检查格式，不修改文件
## uv format --check


# 5.使用mypy检查类型
## 检查当前项目中的Python类型标注
## uv run mypy .

## mypy会检查
##     函数参数类型是否正确
##     函数返回值类型是否正确
##     变量类型是否存在冲突


# 6.检查依赖安全问题
## uv audit
## 该命令会
##     检查项目锁定的依赖是否存在已知安全漏洞
##     默认包含正式依赖和开发依赖


# 7.常用的项目检查步骤
## 1.uv sync                        同步项目依赖
## 2.uv run ruff check .           检查代码问题
## 3.uv run ruff format . --check  检查代码格式
## 4.uv run mypy .                 检查类型标注
## 5.uv run pytest                 运行自动化测试
## 6.uv audit                      检查依赖安全问题
