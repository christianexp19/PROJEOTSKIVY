from flask import Flask, render_template, request, jsonify
import requests

app = Flask(__name__)

API_KEY = "SUA_API_KEY_AQUI"  # Coloque sua chave da OpenWeatherMap

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/clima", methods=["GET"])
def clima():
    cidade = request.args.get("cidade")
    if not cidade:
        return jsonify({"erro": "Informe uma cidade"}), 400

    try:
        url = (
            f"https://api.openweathermap.org/data/2.5/weather"
            f"?q={cidade}&appid={API_KEY}&units=metric&lang=pt_br"
        )
        resp = requests.get(url)
        resp.raise_for_status()
        dados = resp.json()

        resultado = {
            "cidade": dados["name"],
            "temperatura": dados["main"]["temp"],
            "descricao": dados["weather"][0]["description"].capitalize()
        }
        return jsonify(resultado)

    except requests.exceptions.RequestException:
        return jsonify({"erro": "Falha na conexão com a API"}), 500
    except KeyError:
        return jsonify({"erro": "Não foi possível interpretar os dados"}), 500

if __name__ == "__main__":
    app.run(debug=True)
