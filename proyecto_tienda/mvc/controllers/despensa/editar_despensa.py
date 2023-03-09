import web
import sqlite3

render = web.template.render('proyecto_tienda/mvc/views')

class editar_despensa:
    def GET(self,sku):
        with sqlite3.connect("proyecto_tienda/db/despensa.sqlite3") as connection:
            #connection.row_factory: sqlite3.Row
            cursor = connection.cursor()
            #sql = ("select * from productos where sku=?",(sku,))
            cursor.execute("select * from despensa where sku=?",(sku,))
            result = cursor.fetchone()
            print(result[0])
        return render.despensa.actualizar(result)

    def POST(self,sku):
        datos= dict(web.input())
        #return datos["sku"],["unidad"],["nombre"]
        with sqlite3.connect("proyecto_tienda/db/despensa.sqlite3") as connection:
            cursor = connection.cursor()
            despensa_lista = (datos['precio'],datos['fecha'],datos['id_tienda'],sku)
            print (despensa_lista)
            cursor.execute("UPDATE despensa SET precio=?,fecha=?,id_tienda=? WHERE sku=?;",despensa_lista)
            connection.commit()
            raise web.seeother('/despensa')
