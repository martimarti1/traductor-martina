from flask import Flask, request, jsonify, render_template

app = Flask(__name__)

dic = {
    "a": "@",
    "b": "#",
    "c": "*",
    "d": "]",
    "e": "€",
    "f": "₤",
    "g": "&",
    "h": "}-{",
    "i": ".",
    "j": "?",
    "k": "+",
    "l": "!",
    "m": "=",
    "n": "-",
    "o": "()",
    "p": "<",
    "q": "~",
    "r": ";",
    "s": "$",
    "t": ".,",
    "u": "0",
    "v": "|_|",
    "w": "|_|_|",
    "x": "><",
    "y": "¥",
    "z": "7_"
}

def traducir_normal_a_codigo(texto):
    resultado = ""
    for letra in texto.lower():
        resultado += dic.get(letra, letra)
    return resultado

def traducir_codigo_a_normal(texto):
    dic_invertido = {v: k for k, v in dic.items()}
    claves_ordenadas = sorted(dic_invertido.keys(), key=len, reverse=True)
    
    resultado = ""
    i = 0
    
    while i < len(texto):
        match = False
        for simbolo in claves_ordenadas:
            if texto.startswith(simbolo, i):
                resultado += dic_invertido[simbolo]
                i += len(simbolo)
                match = True
                break
        
        if not match:
            resultado += texto[i]
            i += 1
    
    return resultado

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/api/traducir", methods=["POST"])
def api_traducir():
    data = request.get_json()

    texto = data.get("texto", "")
    modo = data.get("modo", "normal_a_codigo")

    if modo == "normal_a_codigo":
        traduccion = traducir_normal_a_codigo(texto)
    else:
        traduccion = traducir_codigo_a_normal(texto)

    return jsonify({"traduccion": traduccion})

if __name__ == "__main__":
    app.run(debug=True)
