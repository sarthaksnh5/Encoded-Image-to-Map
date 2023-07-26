from flask import Flask, request, jsonify, send_file
from PIL import Image
import io
from flask_cors import CORS  # Import the CORS module
import base64

app = Flask(__name__)
CORS(app)

def encode_image(image_path, quality=50):
    img = Image.open(image_path)
    buffered = io.BytesIO()
    img.save(buffered, format='PNG', quality=quality)
    return base64.b64encode(buffered.getvalue())

@app.route('/encode_image', methods=['GET'])
def handle_encode_image():
    image_path = './image.png'  # Path to the high-quality image in the server
    encoded_image = encode_image(image_path, quality=100)  # Adjust quality as needed
    return jsonify({'encoded_image': encoded_image.decode('latin1')})

@app.route('/get_high_quality_image', methods=['GET'])
def get_high_quality_image():
    image_path = './image.png'  # Path to the high-quality image in the server
    return send_file(image_path, mimetype='image/jpeg')


if __name__ == "__main__":
    app.run("0.0.0.0", 8000, debug=True)