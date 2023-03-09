import web
import sqlite3

render = web.template.render('proyecto_tienda/mvc/views')

with sqlite3.connect("proyecto_tienda/db/despensa.sqlite3") as connection:
    cursor = connection.cursor()
    sql = ("select * from tienda")
    cursor.execute(sql)
    result = cursor.fetchall()

regresar= web.url('/tiendas')

class agregar_tienda:
    def GET(self):
        return render.tienda.insertar(regresar)

    def POST(self):
        datos= dict(web.input())
        with sqlite3.connect("proyecto_tienda/db/despensa.sqlite3") as connection:
            cursor = connection.cursor()
            tienda_dispo = (datos['id_tienda'], datos['nombre'])
            print (tienda_dispo)
            cursor.execute("insert into tienda (id_tienda, nombre) values (?,?);",tienda_dispo)
            connection.commit()
        return render.tienda.insertar(regresar)
