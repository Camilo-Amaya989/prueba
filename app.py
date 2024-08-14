from flask import Flask, render_template, request, redirect, url_for

app=Flask(__name__ )

inventario=[ ]

@app.route('/')
def index():
    return render_template('Pagina_Inicio.html', inventario=inventario)

@app.route('/agregar' , methods=[ 'POST' ] )
def agregar():
    nombre= request.form[' nombre ']
    cantidad= int(request.form[ 'cantidad' ])
    inventario.append({' nombre ' : nombre, ' cantidad ' : cantidad  })
    return redirect(url_for('index'))

if __name__ == '__main__' :
    app.run(debug=True)