from git import Git

def update_force(path):
    """
        强制更新 buckets
    """

    g = Git(path)
    info_1 = g.config("--global", "http.proxy", "socks5://127.0.0.1:10808")
    g.checkout('*')
    pull_info = g.pull("--no-rebase")
    g.config("--global", "--unset", "http.proxy")
    return pull_info


