from git import Git

class MyGit():
    def __init__(self, path):
        self.g = Git(path)

    def update_force(self):
        """
            强制更新 buckets
        """
        info_1 = self.g.config("--global", "http.proxy", "socks5://127.0.0.1:10808")
        self.g.checkout('*')
        pull_info = self.g.pull("--no-rebase")
        self.g.config("--global", "--unset", "http.proxy")
        return pull_info


