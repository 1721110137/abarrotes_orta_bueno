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

class mostrar_Despensa:
    def GET(self):
        agregar= web.url('/agregar_despensa')
        with sqlite3.connect("proyecto_tienda/db/despensa.sqlite3") as connection:
            #connection.row_factory: sqlite3.Row
            cursor = connection.cursor()
            sql = ("select * from despensa")
            cursor.execute(sql)
            result = cursor.fetchall()

        return render.despensa.lista(result,agregar)
        
        