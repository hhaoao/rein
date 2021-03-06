from git import Git

class MyGit():
    def __init__(self, path):
        self.g = Git(path)

    def update_force(self, config=None):
        """
            强制更新 buckets
        """
        if 'http.proxy' in config:
            info_1 = self.g.config("--global", "http.proxy", config['git']['http.proxy'])
            self.g.checkout('*')
            pull_info = self.g.pull("--no-rebase")
            self.g.config("--global", "--unset", "http.proxy")
        else:
            self.g.checkout('*')
            pull_info = self.g.pull("--no-rebase")

        return pull_info


