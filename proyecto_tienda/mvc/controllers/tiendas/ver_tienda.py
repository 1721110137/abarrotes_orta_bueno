import web
import sqlite3

render = web.template.render('proyecto_tienda/mvc/views')

with sqlite3.connect("proyecto_tienda/db/despensa.sqlite3") as connection:
    #connection.row_factory: sqlite3.Row
    cursor = connection.cursor()
    sql = ("select * from tienda")
    cursor.execute(sql)
    result = cursor.fetchall()

regresar= web.url('/tiendas')

class mostrar_tienda:
    def GET(self):
        agregar= web.url('/agregar_tienda')
        with sqlite3.connect("proyecto_tienda/db/despensa.sqlite3") as connection:
            #connection.row_factory: sqlite3.Row
            cursor = connection.cursor()
            sql = ("select * from tienda")
            cursor.execute(sql)
            result = cursor.fetchall()

        return render.tienda.lista(result,agregar)
