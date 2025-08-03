from flask import Flask, render_template, request
from algoritmos_busqueda import busqueda_secuencial, busqueda_binaria

app = Flask(__name__)

productos = [
    {"id": 1, "nombre": "Laptop", "precio": 15000},
    {"id": 2, "nombre": "Mouse", "precio": 250},
    {"id": 3, "nombre": "Teclado", "precio": 800},
    {"id": 4, "nombre": "Monitor", "precio": 3500},
    {"id": 5, "nombre": "Audífonos", "precio": 1200},
    {"id": 6, "nombre": "Impresora", "precio": 2800},
    {"id": 7, "nombre": "Webcam", "precio": 950},
]

@app.route('/')
def index():
    return render_template('index.html', productos=productos)

@app.route('/busqueda_secuencial', methods=['GET', 'POST'])
def busqueda_secuencial_route():
    mensaje = None
    posicion = None
    valor = None
    if request.method == 'POST':
        valor = request.form.get('valor')
        try:
            valor = int(valor)
            precios = [p["precio"] for p in productos]
            posicion = busqueda_secuencial(precios, valor)
            mensaje = f"Precio {valor} encontrado." if posicion != -1 else f"Precio {valor} no encontrado."
            if posicion == -1:
                posicion = None
        except:
            mensaje = "Ingrese un valor válido."
    return render_template('busqueda_secuencial.html', productos=productos, mensaje=mensaje, posicion=posicion, valor=valor)

@app.route('/busqueda_binaria', methods=['GET', 'POST'])
def busqueda_binaria_route():
    mensaje = None
    posicion = None
    valor = None
    pasos = []

    if request.method == 'POST':
        valor = request.form.get('valor')
        try:
            valor = int(valor)
            precios = sorted([p["precio"] for p in productos])
            izquierda, derecha = 0, len(precios) - 1

            while izquierda <= derecha:
                medio = (izquierda + derecha) // 2
                pasos.append({
                    "rango": f"[{izquierda}, {derecha}]",
                    "medio": medio,
                    "valor_medio": precios[medio],
                    "buscado": valor
                })

                if precios[medio] == valor:
                    posicion = medio
                    break
                elif precios[medio] < valor:
                    izquierda = medio + 1
                else:
                    derecha = medio - 1

            mensaje = f"Precio {valor} encontrado." if posicion is not None else f"Precio {valor} no encontrado."
        except:
            mensaje = "Ingrese un valor válido."

    return render_template('busqueda_binaria.html',
                           productos=sorted(productos, key=lambda x: x["precio"]),
                           mensaje=mensaje,
                           posicion=posicion,
                           valor=valor,
                           pasos=pasos)


if __name__ == '__main__':
    app.run(debug=True)
