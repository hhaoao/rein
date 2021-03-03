import sqlite3
import re

def regexp(expr, item):
    reg = re.compile(expr)
    return reg.search(item) is not None

class sqlite():
    """
        使用sqlite3 数据库 创建packages 仓库
        顺序:
            init
            create_table
            query

    """

    def __init__(self):
        self.database = ":memory:"
        self.init_table = "CREATE TABLE manager(name, bucket)"
        self.conn = None
            

    def create_table(self):
        self.conn = sqlite3.connect(self.database)
        self.conn.create_function("REGEXP", 2, regexp)
        # Create the table
        self.conn.execute(self.init_table)

    def packages_storage(self, packages): 
        self.conn.executemany("INSERT OR IGNORE INTO manager(name, bucket) VALUES (?,?)", packages)

    def query(self, package):
        """
            查询单个包, 输入的包名必须完全匹配.
        """

        target = self.conn.execute("SELECT * FROM manager WHERE name=?", (package,))
        return target.fetchall()

    def query_regex(self, package):
        """
            正则查询 包
        """
        target = self.conn.execute('SELECT * FROM manager WHERE name REGEXP ?', (package,))
        return target.fetchall()
