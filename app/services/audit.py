import json
import sqlite3
from datetime import datetime,timezone
from app.core.config import get_settings

settings=get_settings()

def init_db()->None:
    conn=sqlite3.connect(settings.audit_db_path)
    cursor=conn.cursor()
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS audit_log (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        timestamp TEXT NOT NULL,
        question TEXT NOT NULL,
        source_used TEXT NOT NULL,
        trace TEXT NOT NULL
    )
    """)
    conn.commit()
    conn.close()

def write_audit(question:str,source_used:str,trace:list[str])->None:
    conn=sqlite3.connect(settings.audit_db_path)
    cursor=conn.cursor()
    timestamp=datetime.now(timezone.utc).isoformat()
    trace_json=json.dumps(trace)
    cursor.execute("""
    INSERT INTO audit_log (timestamp, question, source_used, trace)
    VALUES (?, ?, ?, ?)
    """,(timestamp,question,source_used,trace_json))
    conn.commit()
    conn.close()