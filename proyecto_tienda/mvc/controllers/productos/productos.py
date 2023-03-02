import web
import sqlite3

render = web.template.render('proyecto_tienda/mvc/views')

class mProductos:
    def GET(self):
        with sqlite3.connect("proyecto_tienda/db/despensa.sqlite3") as connection:
            #connection.row_factory: sqlite3.Row
            cursor = connection.cursor()
            sql = ("select * from productos")
            cursor.execute(sql)
            result = cursor.fetchall()

        return render.productos.lista(result)