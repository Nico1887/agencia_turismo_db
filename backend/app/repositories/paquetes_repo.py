from app.db.database import get_connection



def obtener_paquetes(precio_min=None, nivelServicio=None, offset=0, size=10):
    conn = get_connection()
    cursor = conn.cursor()

    #Base de la consulta
    base_query = """
        FROM Paquete
        WHERE 1=1
    """

    params = []

    #Filtros dinámicos
    if precio_min is not None:
        base_query += " AND Precio >= ?"
        params.append(precio_min)

    if nivelServicio is not None:
        base_query += " AND NivelServicioID = ?"
        params.append(nivelServicio)

    count_query = "SELECT COUNT(*) " + base_query
    cursor.execute(count_query, params)
    total = cursor.fetchone()[0]

    paginated_query = """
        SELECT PaqueteID, Descripcion, Precio, NivelServicioID, CupoMaximo
    """ + base_query + """
        ORDER BY PaqueteID
        OFFSET ? ROWS
        FETCH NEXT ? ROWS ONLY
    """

    paginated_params = params + [offset, size]

    cursor.execute(paginated_query, paginated_params)

    paquetes = []

    for row in cursor.fetchall():
        paquetes.append({
            "id": row.PaqueteID,
            "nombre": row.Descripcion,
            "precio": row.Precio,
            "nivelServicio": row.NivelServicioID,
            "cupo": row.CupoMaximo
        })

    conn.close()

    return paquetes, total

def create_paquete(paquete):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(
        """
        INSERT INTO Paquete (Descripcion, Precio, NivelServicioID, CupoMaximo)
        OUTPUT INSERTED.PaqueteID, INSERTED.Descripcion, INSERTED.Precio, INSERTED.NivelServicioID, INSERTED.CupoMaximo
        VALUES (?, ?, ?, ?)
        """,
        paquete.nombre, paquete.precio, paquete.nivelServicio, paquete.cupo
    )
    row = cursor.fetchone()
    conn.commit()
    conn.close()

    return {
        "id": row[0],
        "nombre": row[1],
        "precio": row[2],
        "nivelServicio": row[3],
        "cupo": row[4]
    }

def obtener_paquete_via_ID(id : int):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(
        """
        SELECT PaqueteID, Descripcion, Precio, NivelServicioID, CupoMaximo
        FROM Paquete
        WHERE PaqueteID = ?
        """, id
    )
    resultadoConsulta = cursor.fetchone()
    if resultadoConsulta is None:
        return None
    else:
        paquete_resultado =  {
        'id' : resultadoConsulta[0],
        'nombre' : resultadoConsulta[1],
        'precio' : resultadoConsulta[2],
        'nivelServicio' : resultadoConsulta[3],
        'cupo' : resultadoConsulta[4]
        }
    conn.close()
    return paquete_resultado
    
def elimacion_fisica_paquete(id):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(
        """
        DELETE FROM Paquete WHERE PaqueteID = ?
        """, id
    )
    cursor.commit()
    conn.close

    filas_afectadas = cursor.rowcount
    return filas_afectadas > 0

def actualizacion_paquete(id, nuevos_datos):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(
        """
        SELECT PaqueteID, Descripcion FROM Paquete WHERE PaqueteID = ?
        """, id)
    
    resultadoConsulta = cursor.fetchone()
    if resultadoConsulta is None:
        conn.close()
        return None
    
    cursor.execute(
        """
        UPDATE Paquete
        SET
        Descripcion = ?,
        Precio = ?,
        NivelServicioID = ?,
        CupoMaximo = ?
        WHERE PaqueteID = ?
        """, nuevos_datos.nombre, nuevos_datos.precio, nuevos_datos.nivelServicio, nuevos_datos.cupo, id
    )
    conn.commit()


    cursor.execute(
        """
        SELECT PaqueteID, Descripcion, Precio, NivelServicioID, CupoMaximo FROM Paquete WHERE PaqueteID = ?
        """, id)
    resultadoConsulta = cursor.fetchone()

    datos_actualizados = {
        'id' : resultadoConsulta[0],
        'nombre' : resultadoConsulta[1],
        'precio' : resultadoConsulta[2],
        'nivelServicio' : resultadoConsulta[3],
        'cupo' : resultadoConsulta[4]
        }

    conn.close()
    return datos_actualizados