# main.py
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List, Optional
from db import get_connection
import logging

app = FastAPI()

# Configurar el logger (log de errores)
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class Item(BaseModel):
    id: str
    nombre: str
    cosa: Optional[str] = None

'''Esta línea define una clase Item que representa un modelo de datos con tres campos: id, nombre, y cosa. 
Cada uno de estos campos tiene un tipo específico y cosa puede ser opcionalmente nulo. 
Este modelo se puede utilizar para validar y serializar datos en las solicitudes y respuestas de tu API.
'''

@app.get("/items/", response_model=List[Item])
def read_items():
    try:
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute('SELECT id, nombre, cosa FROM Tabla_prueba')
        rows = cursor.fetchall()
        items = [Item(id=row[0], nombre=row[1], cosa=row[2]) for row in rows]
        conn.close()
        return items
    except Exception as e:
        logger.error(f"Error al leer los items: {e}")
        raise HTTPException(status_code=500, detail="Internal Server Error")

@app.get("/items/{item_id}", response_model=Item)
def read_item(item_id: str):
    try:
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute('SELECT id, nombre, cosa FROM Tabla_prueba WHERE id = ?', item_id)
        row = cursor.fetchone()
        conn.close()
        if row:
            return Item(id=row[0], nombre=row[1], cosa=row[2])
        else:
            raise HTTPException(status_code=404, detail="Item not found")
    except Exception as e:
        logger.error(f"Error al leer el item con id {item_id}: {e}")
        raise HTTPException(status_code=500, detail="Internal Server Error")

if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000, debug=True, reload=True)