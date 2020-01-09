from git import Repo
repo = Repo("./")
print(repo.active_branch)
repo.index.add(["test.py"])
repo.index.commit("创建test文件")
