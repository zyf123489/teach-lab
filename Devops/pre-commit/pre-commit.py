# pre-commit 是Git的钩子工具，用于每次执行git commit 之前，自动运行一系列检查脚本
# 不通过就不给提交

# 工作流程：
## git add .
## git commit -m "commit message"
## 触发pre-commit 钩子
## 自动执行 格式化、语法检查、导入排序、清理尾随空格等
## 任意一项失败 → 终止 commit，代码提交不成功

# 常用搭配
## ruff 用于检查代码格式和语法
## mypy 用于检查类型标注

# 使用步骤
## 1.安装pre-commit
## pip install pre-commit 或者 uv add --dev pre-commit
## 2.项目根目录新建文件: .pre-commit-config.yaml
##      粘贴下面常用模板（ruff 代码检查 + 格式化）

##      repos:
##        - repo: https://github.com/astral-sh/ruff-pre-commit
##          rev: v0.7.0
##          hooks:
##            - id: ruff        # 代码静态检查、自动修复简单问题
##            - id: ruff-format # 代码自动格式化
##
##后续想加 mypy、yaml 检查都可以继续追加配置。

## 3.初始化pre-commit
## 作用：往 .git/hooks 写入脚本；以后执行 git commit 自动触发检查。
## (一个项目只需要执行一次，但是换电脑、重新克隆项目，需要再次执行)
## pre-commit install / uv run pre-commit install

## 以后在执行 git commit 时，会自动触发检查
## 检查通过 → 提交成功
## 检查失败 → 终止 commit，代码提交不成功
