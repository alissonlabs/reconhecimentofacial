import face_recognition
from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app) # Permite que o nosso HTML acesse essa API

@app.route('/compare', methods=['POST'])
def compare_faces():
    # Recebe os arquivos enviados pelo JavaScript
    file1 = request.files.get('image1')
    file2 = request.files.get('image2')

    if not file1 or not file2:
        return jsonify({"error": "Envie duas imagens"}), 400

    try:
        # Carrega as imagens no formato que a biblioteca entende
        img1 = face_recognition.load_image_file(file1)
        img2 = face_recognition.load_image_file(file2)

        # Extrai o vetor matemático do rosto (pega o primeiro rosto encontrado)
        encodings1 = face_recognition.face_encodings(img1)
        encodings2 = face_recognition.face_encodings(img2)

        if not encodings1 or not encodings2:
            return jsonify({"error": "Rosto não detectado em uma das fotos"})

        # Compara as duas assinaturas matemáticas
        match = face_recognition.compare_faces([encodings1[0]], encodings2[0])[0]
        distance = face_recognition.face_distance([encodings1[0]], encodings2[0])[0]

        # Distância menor que 0.6 geralmente significa a mesma pessoa
        return jsonify({
            "match": bool(match), 
            "distance": float(distance)
        })
        
    except Exception as e:
        return jsonify({"error": str(e)})

if __name__ == '__main__':
    app.run(debug=True, port=5000)