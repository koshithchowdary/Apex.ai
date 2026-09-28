import sqlite3
from pathlib import Path
class Memory:
    def __init__(self,path=".apex/memory.db"):
        Path(path).parent.mkdir(parents=True,exist_ok=True)
        self.db=sqlite3.connect(path,check_same_thread=False)
        self.db.execute("CREATE TABLE IF NOT EXISTS messages(id INTEGER PRIMARY KEY,role TEXT,content TEXT)")
        self.db.commit()
    def add(self,role,content):
        self.db.execute("INSERT INTO messages(role,content) VALUES(?,?)",(role,content)); self.db.commit()
    def recent(self,limit=12):
        r=self.db.execute("SELECT role,content FROM messages ORDER BY id DESC LIMIT ?",(limit,)).fetchall()
        return list(reversed(r))
    def clear(self):
        self.db.execute("DELETE FROM messages"); self.db.commit()
