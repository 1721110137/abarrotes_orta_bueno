import web
import sqlite3

render = web.template.render('proyecto_tienda/mvc/views')

with sqlite3.connect("proyecto_tienda/db/despensa.sqlite3") as connection:
    #connection.row_factory: sqlite3.Row
    cursor = connection.cursor()
    sql = ("select * from productos")
    cursor.execute(sql)
    result = cursor.fetchall()

regresar= web.url('/productos')


class agregar_productos:
    def GET(self):
        return render.productos.insertar(regresar)

    def POST(self):
        datos= dict(web.input())
        #return datos["sku"],["unidad"],["nombre"]
        with sqlite3.connect("proyecto_tienda/db/despensa.sqlite3") as connection:
            cursor = connection.cursor()
            productos_lista = (datos['sku'],datos['nombre'],datos['unidad'])
            print (productos_lista)
            cursor.execute("insert into productos (sku,nombre_producto,unidad) values (?,?,?);",productos_lista)
            connection.commit()
        return render.productos.insertar(regresar)