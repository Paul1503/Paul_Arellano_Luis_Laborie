def total_carrito(request):
    total = 0
    if 'carrito' in request.session:
        try:
            carrito = request.session['carrito']
            for key, value in carrito.items():
                precio = int(value['precio'])
                cantidad = value['cantidad']
                subtotal = precio * cantidad
                total += subtotal
        except KeyError:
            request.session['carrito'] = {}
            total = 0
    return {'total_carrito': total}
