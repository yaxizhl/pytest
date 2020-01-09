from git import Repo
repo = Repo("./")
remote = repo.remote()

print(repo.is_dirty())
if repo.is_dirty():
    # print(repo.active_branch)
    repo.git.add(A=True)
    repo.git.commit("-m", "update")
    remote.push()
