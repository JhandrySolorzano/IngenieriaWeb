# Archivo para conexión a base de datos
import pymysql

# Conexión
try:
    com = pymysql.connect(
        host='localhost',
        user='root',
        passwd='123456789',
        database='universidad',
        port=3306
    )

    def consultar_modalidades():
        with com.cursor() as cursor:
            cursor.execute('SELECT * FROM modalidad')
            resultados = cursor.fetchall()
            for fila in resultados:
                print(fila[1])

    def insertar_carrera():
        with com.cursor() as cursor:
            cursor.execute("INSERT INTO carrera(codigo, nombre, modalidad_id) VALUES('COMP_01', 'Computacion', 1)")      
        com.commit()

    def actualizar_nombre_carrera(codigo, nuevo_nombre):
        with com.cursor() as cursor:
            cursor.execute("UPDATE carrera SET nombre = %s WHERE codigo = %s", (nuevo_nombre, codigo))
        com.commit()
        print(f"Carrera con código {codigo} actualizada a {nuevo_nombre}.")

    def eliminar_carrera_por_id(carrera_id):
        with com.cursor() as cursor:
            cursor.execute("DELETE FROM carrera WHERE id = %s", (carrera_id,))
        com.commit()
        print(f"Carrera con id {carrera_id} eliminada.")

    def contar_carreras():
        with com.cursor() as cursor:
            cursor.execute("SELECT COUNT(*) FROM carrera")
            (total,) = cursor.fetchone()
        print(f"Número total de registros en la tabla 'carrera': {total}")

    def consultar_carreras():
        with com.cursor() as cursor:
            cursor.execute('SELECT * FROM carrera')
            resultados = cursor.fetchall()
            for fila in resultados:
                print(fila[0], ' - ', fila[1], ' - ', fila[2])

    # Ejecución de funciones
    insertar_carrera()
    actualizar_nombre_carrera('COMP_01', 'Ingeniería en Computación')
    consultar_carreras()
    contar_carreras()
    eliminar_carrera_por_id(1)  # Cambia el ID según los registros existentes
    consultar_carreras()
    consultar_modalidades()

except pymysql.MySQLError as e:
    print("Error en la conexión o en las consultas:", e)

finally:
    # Cerrar la conexión a la base de datos
    if com and com.open:
        com.close()
