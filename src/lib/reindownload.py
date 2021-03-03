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
            secret=""
        )

        self.aria2 = aria2p.API(
            self.client
        )

    def add_urls(self, url=[]):
        self.aria2.add_uris(url)

