from git import Repo
repo = Repo("./")

print(repo.is_dirty())
if repo.is_dirty():
    print(repo.active_branch)
    repo.index.add(["test.py"])
    repo.index.commit("update")
    repo.index.push()
