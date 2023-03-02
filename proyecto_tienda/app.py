import web

urls = (
    '/', 'mvc.controllers.bienvenida.index.Index',
    '/productos', 'mvc.controllers.productos.productos.mProductos'
)
app = web.application(urls, globals()) #aplicacion web

if __name__ == "__main__":
    app.run()
