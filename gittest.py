from git import Repo
repo = Repo("./")
remote = repo.remote()

print(repo.is_dirty())
if repo.is_dirty():
    print(repo.active_branch)
    repo.index.add(["gittest.py"])
    repo.index.commit("update")
    remote.push()
