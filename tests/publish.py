import os
import json
from flask import Flask, request, jsonify

app = Flask(__name__)

TEMPLATE_PATH = "template.html"
TESTS_DIR = "tests/"

@app.route("/publish.py", methods=["POST"])
def publish():
    data = request.json
    test_id = data["testId"]
    task = data["task"]
    figma_url = data["figmaUrl"]

    # Читаем шаблон
    with open(TEMPLATE_PATH, "r", encoding="utf-8") as f:
        template = f.read()

    # Заменяем переменные
    test_page = template.replace("{{ task }}", task).replace("{{ figmaUrl }}", figma_url)

    # Сохраняем HTML-файл
    os.makedirs(TESTS_DIR, exist_ok=True)
    with open(f"{TESTS_DIR}/{test_id}.html", "w", encoding="utf-8") as f:
        f.write(test_page)

    return jsonify({"url": f"tests/{test_id}.html"})

if __name__ == "__main__":
    app.run(debug=True)
