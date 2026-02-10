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

def create_paquete(paquete):
    conn = get_connection()
    cursor = conn.cursor()

    if paquete.id is not None:
        cursor.execute("SET IDENTITY_INSERT Paquete ON")
        cursor.execute("""
            INSERT INTO Paquete (PaqueteID, Descripcion, Precio, NivelServicioID, CupoMaximo)
            OUTPUT INSERTED.PaqueteID
            VALUES (?, ?, ?, ?, ?)
        """, paquete.id, paquete.nombre, paquete.precio, paquete.nivelServicio, paquete.cupo)
        paquete_id = cursor.fetchone()[0]
        cursor.execute("SET IDENTITY_INSERT Paquete OFF")
    else:
        cursor.execute("""
            INSERT INTO Paquete (Descripcion, Precio, NivelServicioID, CupoMaximo)
            OUTPUT INSERTED.PaqueteID
            VALUES (?, ?, ?, ?)
        """, paquete.nombre, paquete.precio, paquete.nivelServicio, paquete.cupo)
        paquete_id = cursor.fetchone()[0]

    conn.commit()
    conn.close()
    return {
        'id' : paquete_id,
        'nombre' : paquete.nombre,
        'precio' : paquete.precio,
        'cupo' : paquete.cupo
    }