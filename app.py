import os
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return "Hello, World! Flask App on Render!!!!!!!!!"

if __name__ == "__main__":
    # Render が指定する PORT 環境変数を使ってポートを設定
    port = int(os.environ.get("PORT", 5000))  # PORT環境変数を使用、無ければ5000
    app.run(host="0.0.0.0", port=port, debug=False)  # 0.0.0.0で外部アクセスを許可