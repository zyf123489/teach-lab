# uv可以构建和发布Python包，也可以使用workspace管理包含多个子项目的仓库

# 1.创建可以打包的Python项目
## uv init --package 项目名
## 例如 uv init --package uv-demo
## 该命令会创建适合Python包的src目录结构和构建配置

## 包项目的常见目录结构
## uv-demo/
##     pyproject.toml
##     README.md
##     src/
##         uv_demo/
##             __init__.py

## 普通的 uv init 默认创建应用项目
## 需要构建和发布的库项目优先使用 uv init --package


# 2.管理项目版本
## 查看当前项目版本
## uv version

## 设置指定版本
## uv version 1.0.0

## 按语义化版本规则升级版本
## uv version --bump patch    例如从1.0.0升级到1.0.1
## uv version --bump minor    例如从1.0.0升级到1.1.0
## uv version --bump major    例如从1.0.0升级到2.0.0

## 项目版本会保存在 pyproject.toml 的 project.version 中


# 3.构建Python包
## uv build
## 该命令会
##     读取 pyproject.toml 中的项目和构建配置
##     在 dist 目录生成源码包 .tar.gz
##     在 dist 目录生成wheel包 .whl

## 每次正式构建前应该先运行
## uv sync
## uv run pytest
## uv build


# 4.发布Python包
## 发布前需要
##     在PyPI注册账号
##     创建一个没有被其他人使用的项目名
##     创建PyPI发布令牌
##     确认dist目录中的构建文件正确

## 先检查发布过程，但不真正上传
## uv publish --dry-run

## PowerShell中通过环境变量临时设置PyPI令牌
## $env:UV_PUBLISH_TOKEN = "PyPI令牌"

## 发布dist目录中的包到PyPI
## uv publish

## 不要把PyPI令牌写入Python代码、pyproject.toml或提交到Git


# 5.理解workspace
## workspace用于在一个仓库中管理多个相互关联的Python项目
## 所有workspace成员共享一个uv.lock和一个项目虚拟环境

## workspace常见目录结构
## project-root/
##     pyproject.toml
##     uv.lock
##     packages/
##         app/
##             pyproject.toml
##         common/
##             pyproject.toml

## 在根目录pyproject.toml中声明workspace成员
## [tool.uv.workspace]
## members = ["packages/*"]


# 6.管理workspace成员
## 同步整个workspace
## uv sync --all-packages

## 给指定成员添加普通依赖
## uv add requests --package app

## 把workspace中的common添加为app的依赖
## uv add common --package app --workspace

## 在指定成员中运行命令
## uv run --package app python main.py

## 构建指定workspace成员
## uv build --package common


# 7.打包和发布的常用步骤
## 1.uv init --package uv-demo   创建包项目
## 2.uv add 依赖名               添加正式依赖
## 3.uv add --dev pytest ruff    添加开发依赖
## 4.uv run pytest               运行测试
## 5.uv version --bump patch     更新项目版本
## 6.uv build                    构建源码包和wheel包
## 7.uv publish --dry-run        检查发布过程
## 8.uv publish                  发布到PyPI
