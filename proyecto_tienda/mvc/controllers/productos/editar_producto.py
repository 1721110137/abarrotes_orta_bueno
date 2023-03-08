import web
import sqlite3

render = web.template.render('proyecto_tienda/mvc/views')

class editar_productos:
    def GET(self,sku):
        with sqlite3.connect("proyecto_tienda/db/despensa.sqlite3") as connection:
            #connection.row_factory: sqlite3.Row
            cursor = connection.cursor()
            #sql = ("select * from productos where sku=?",(sku,))
            cursor.execute("select * from productos where sku=?",(sku,))
            result = cursor.fetchone()
            print(result[0])
        return render.productos.actualizar(result)

    def POST(self,sku):
        datos= dict(web.input())
        #return datos["sku"],["unidad"],["nombre"]
        with sqlite3.connect("proyecto_tienda/db/despensa.sqlite3") as connection:
            cursor = connection.cursor()
            productos_lista = (datos['nombre'],datos['unidad'],sku)
            print (productos_lista)
            cursor.execute("UPDATE productos SET nombre_producto=?,unidad=? WHERE sku=?;",productos_lista)
            connection.commit()
            raise web.seeother('/productos')