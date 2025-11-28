<<<<<<< HEAD
from flask import Flask, request, jsonify, render_template
from datetime import datetime

app = Flask(__name__)

yorumlar = []  # yorumları tutacak basit liste

@app.route('/')
def blog():
    return render_template('blog.html')

@app.route('/yorumlar', methods=['GET','POST'])
def yorumlar_route():
    if request.method == 'POST':
        data = request.get_json()
        yorumlar.append({
            "isim": data.get('isim'),
            "yorum": data.get('yorum'),
            "tarih": datetime.now().isoformat()
        })
        return jsonify({"ok": True})
    return jsonify(yorumlar)

if __name__ == '__main__':
    app.run(debug=True)
=======
from flask import Flask, request, jsonify, render_template
from datetime import datetime

app = Flask(__name__)

yorumlar = []  # yorumları tutacak basit liste

@app.route('/')
def blog():
    return render_template('blog.html')

@app.route('/yorumlar', methods=['GET','POST'])
def yorumlar_route():
    if request.method == 'POST':
        data = request.get_json()
        yorumlar.append({
            "isim": data.get('isim'),
            "yorum": data.get('yorum'),
            "tarih": datetime.now().isoformat()
        })
        return jsonify({"ok": True})
    return jsonify(yorumlar)

if __name__ == '__main__':
    app.run(debug=True)
>>>>>>> 5c73bacda2d0165f483fe3c60fdc85eb8e8ab977
