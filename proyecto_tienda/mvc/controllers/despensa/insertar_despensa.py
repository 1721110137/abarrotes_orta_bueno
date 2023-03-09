import web
import sqlite3

render = web.template.render('proyecto_tienda/mvc/views')

with sqlite3.connect("proyecto_tienda/db/despensa.sqlite3") as connection:
    #connection.row_factory: sqlite3.Row
    cursor = connection.cursor()
    sql = ("select * from despensa")
    cursor.execute(sql)
    result = cursor.fetchall()

regresar= web.url('/despensa')


class agregar_despensa:
    def GET(self):
        return render.despensa.insertar(regresar)

    def POST(self):
        datos= dict(web.input())
        #return datos["sku"],["unidad"],["nombre"]
        with sqlite3.connect("proyecto_tienda/db/despensa.sqlite3") as connection:
            cursor = connection.cursor()
            despensa_lista = (datos['sku'],datos['precio'],datos['fecha'],datos['id_tienda'])
            print (despensa_lista)
            cursor.execute("insert into despensa (sku,precio,fecha,id_tienda) values (?,?,?,?);",despensa_lista)
            connection.commit()
        return render.despensa.insertar(regresar)