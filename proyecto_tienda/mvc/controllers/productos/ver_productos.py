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

class mostrar_Productos:
    def GET(self):
        agregar= web.url('/agregar_productos')
        with sqlite3.connect("proyecto_tienda/db/despensa.sqlite3") as connection:
            #connection.row_factory: sqlite3.Row
            cursor = connection.cursor()
            sql = ("select * from productos LIMIT 5")
            cursor.execute(sql)
            result = cursor.fetchall()

        return render.productos.lista(result,agregar)

    def POST(self):
        sku= web.input()
        with sqlite3.connect("proyecto_tienda/db/despensa.sqlite3") as connection:
            #connection.row_factory: sqlite3.Row
            cursor = connection.cursor()
            #sql = ("SELECT * FROM productos WHERE sku=?",sku["bus_sku"])
            cursor.execute("SELECT * FROM productos WHERE sku=?",(sku["bus_sku"],))
            result = cursor.fetchone()
            print (result)

            if result is None:
                return ("SKU no se encuentra en la base de datos")
            else:
                return render.productos.buscar(result)


#class buscar_sku:
    #def POST(self,sku):
        #sku= web.input()
        #with sqlite3.connect("proyecto_tienda/db/despensa.sqlite3") as connection:
            #connection.row_factory: sqlite3.Row
            #cursor = connection.cursor()
            #sql = ("SELECT * FROM productos WHERE sku=?",sku["bus_sku"])
            #cursor.execute(sql)
            #result = cursor.fetchall()
            #return render.productos.buscar(result)

        
        