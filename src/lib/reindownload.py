import aria2p


class ReinDownload:
    """
    通过RPC下载安装包.
        add_urls:
            添加安装包列表
    """
    def __init__(self):
        self.client = aria2p.Client(
            host="http://localhost",
            port=6800,
            secret="rein"
        )

        self.aria2 = aria2p.API(
            self.client
        )

    def get_version(self):
        return self.client.get_version()

    def add_urls(self, url=[]):
        self.aria2.add_uris(url)

    def tell_status(self):
        gid = self.client.tell_active(keys=["gid"])[0]['gid']
        status = self.client.tell_status(gid, keys=['status'])['status']
        return status
