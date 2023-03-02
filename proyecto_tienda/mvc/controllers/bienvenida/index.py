import web

render = web.template.render('proyecto_tienda/mvc/views')
class Index:
    def GET(self):
        return render.bienvenida.bienvenida()


