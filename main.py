from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import sqlite3

app = FastAPI()

# CORS ayarlarını yapılandırma
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Tüm kaynaklardan erişime izin vermek için "*" kullanabilirsiniz. Daha güvenli bir yapı için doğru etki alanlarını belirtin.
    allow_methods=["GET"],
    allow_headers=["*"],
)

@app.get("/rows")
def get_rows():
    conn = sqlite3.connect('database.sqlite3')
    c = conn.cursor()
    c.execute("SELECT id, row_data FROM rows")
    rows = c.fetchall()
    conn.close()

    formatted_rows = [{"id": row[0], "row_data": row[1]} for row in rows]
    return {"rows": formatted_rows}
