from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def inicio():
    return render_template('index.html')

@app.route('/iniciosession', methods=['GET', 'POST'])
def iniciosession():
    if request.method == 'POST':
        usuario = str(request.form['usuario'])
        clave = str(request.form['clave'])
        if usuario == 'juan' and clave == 'admin':
            mensaje = 'Bienvenido administrador juan'
        elif usuario == 'pepe' and clave == 'user':
            mensaje = 'Bienvenido usuario pepe'
        else:
            mensaje = 'Usuario o contraseña incorrecta'
        return render_template('iniciosession.html', mensaje=mensaje)
    return render_template('iniciosession.html')

@app.route('/compras', methods=['GET', 'POST'])
def compras():
    if request.method == 'POST':
        resultado = ''
        nombre = str(request.form['nombre'])
        edad = int(request.form['edad'])
        cantidad = int(request.form['can_tarros'])
        precio    = (cantidad * 9000)
        if edad < 18:
            descuento = '0'
            mensaje =  'Nombre del cliente: ' + nombre
            mensaje2 = 'Total Sin descuento: $' + str(precio)
            mensaje3 = 'El descuento es de : $' + descuento
            mensaje4 = 'El total a pagar es de: $' + str(precio)

        elif edad > 17 and edad < 31:
            descuento = float((precio * 15)/ 100)
            mensaje = 'Nombre del cliente: ' + nombre
            mensaje2 = 'Total sin descuentos: $' + str(precio)
            mensaje3 = 'El descuento es de : $' + str(descuento)
            mensaje4 = 'El total a pagar es de: $' + str(precio - descuento)
        elif edad > 30:
            descuento = float((precio * 25)/100)
            mensaje = 'Nombre del cliente: ' + nombre
            mensaje2 = 'Total sin descuentos: $' + str(precio)
            mensaje3 = 'El descuento es de : $' + str(descuento)
            mensaje4 = 'El total a pagar es de: $' + str(precio - descuento)
        else:
            mensaje = 'Los campo edad debe ser completado.'
            mensaje2 = ''
            mensaje3 = ''
            mensaje4 = ''
        return render_template('compras.html', mensaje=mensaje, mensaje2=mensaje2, mensaje3=mensaje3, mensaje4=mensaje4)
    return render_template('compras.html')

if __name__ == '__main__':
    app.run(debug=True)