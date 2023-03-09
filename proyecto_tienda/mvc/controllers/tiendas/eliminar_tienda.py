import web
import sqlite3

render = web.template.render('proyecto_tienda/mvc/views')

class eliminar_tienda:

    def GET(self,id_tienda):
        with sqlite3.connect("proyecto_tienda/db/despensa.sqlite3") as connection:
            cursor = connection.cursor()
            cursor.execute("DELETE FROM tienda WHERE id_tienda=?",(id_tienda,))
            connection.commit()
            print("Tienda eliminada")
            raise web.seeother('/tiendas')
