import web
import sqlite3

render = web.template.render('proyecto_tienda/mvc/views')

class eliminar_despensa:

    def GET(self,sku):
        with sqlite3.connect("proyecto_tienda/db/despensa.sqlite3") as connection:
            #connection.row_factory: sqlite3.Row
            cursor = connection.cursor()
            #sql = ("DELETE FROM productos WHERE sku=?",(sku,))
            cursor.execute("DELETE FROM despensa WHERE sku=?",(sku,))
            connection.commit()
            print("registro eliminado")
            raise web.seeother('/despensa')
