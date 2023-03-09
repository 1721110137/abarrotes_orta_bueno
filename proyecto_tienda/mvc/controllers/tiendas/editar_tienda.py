import web
import sqlite3

render = web.template.render('proyecto_tienda/mvc/views')

class editar_tienda:
    def GET(self,id_tienda):
        with sqlite3.connect("proyecto_tienda/db/despensa.sqlite3") as connection:
            cursor = connection.cursor()
            cursor.execute("select * from tienda WHERE id_tienda=?",(id_tienda,))
            result = cursor.fetchone()
        return render.tienda.actualizar(result)

    def POST(self,id_tienda):
        datos= dict(web.input())
        with sqlite3.connect("proyecto_tienda/db/despensa.sqlite3") as connection:
            cursor = connection.cursor()
            tienda_lista = (datos['nombre'],id_tienda)
            print (tienda_lista)
            cursor.execute("UPDATE tienda SET nombre=? WHERE id_tienda=?;",tienda_lista)
            connection.commit()
            raise web.seeother('/tiendas')
