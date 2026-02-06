from app.db.database import get_connection


def obtener_paquetes():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT PaqueteID, Descripcion, Precio, CupoMaximo
        FROM Paquete
    """)

    paquetes = []

    for row in cursor.fetchall():
        paquetes.append({
            "id": row.PaqueteID,
            "nombre": row.Descripcion,
            "precio": row.Precio,
            "cupo": row.CupoMaximo
        })

    conn.close()
    return paquetes