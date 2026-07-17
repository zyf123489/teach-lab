import casbin


enforcer = casbin.Enforcer("model.conf", "policy.csv")

checks = [
    ("alice", "article", "read"),
    ("alice", "article", "write"),
    ("bob", "article", "read"),
    ("bob", "article", "write"),
]

for subject, object_, action in checks:
    allowed = enforcer.enforce(subject, object_, action)

    print(
        f"{subject} -> {action} {object_}: "
        f"{'允许' if allowed else '拒绝'}"
    )