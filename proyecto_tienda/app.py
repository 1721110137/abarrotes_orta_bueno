import web
from web import form
urls = (
    '/', 'mvc.controllers.bienvenida.index.Index',
    '/productos', 'mvc.controllers.productos.ver_productos.mostrar_Productos',
    '/agregar_productos', 'mvc.controllers.productos.insertar_productos.agregar_productos',
    '/eliminar_producto/(\d+)', 'mvc.controllers.productos.eliminar_productos.eliminar_productos',
    '/editar_producto/(\d+)', 'mvc.controllers.productos.editar_producto.editar_productos',
    '/despensa', 'mvc.controllers.despensa.ver_despensa.mostrar_Despensa',
    '/agregar_despensa', 'mvc.controllers.despensa.insertar_despensa.agregar_despensa',
    '/editar_despensa/(\d+)', 'mvc.controllers.despensa.editar_despensa.editar_despensa',
    '/eliminar_despensa/(\d+)', 'mvc.controllers.despensa.eliminar_despensa.eliminar_despensa',
    
     '/tiendas', 'mvc.controllers.tiendas.ver_tienda.mostrar_tienda',
    '/agregar_tienda', 'mvc.controllers.tiendas.insertar_tienda.agregar_tienda',
    '/eliminar_tienda/(\d+)', 'mvc.controllers.tiendas.eliminar_tienda.eliminar_tienda',
    '/editar_tienda/(\d+)', 'mvc.controllers.tiendas.editar_tienda.editar_tienda',
    
    
)
app = web.application(urls, globals()) #aplicacion web

if __name__ == "__main__":
    app.run()
