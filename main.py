from flask import Flask, render_template
import random

app = Flask(__name__)

# Domínio do Render (substitua pelo seu domínio real)
BASE_URL = "https://custom-site-3gur.onrender.com/static"

# Lista de vídeos com URLs completas
videos = {
    'alone': f'{BASE_URL}/videos/alone.mp4',
    'girl playing': f'{BASE_URL}/videos/girl.mp4',
    'girl sleeping': f'{BASE_URL}/videos/girl-sleeping.mp4',
    'mountain': f'{BASE_URL}/videos/mountain.mp4',
    'solo leveling': f'{BASE_URL}/videos/solo-leveling.mp4',
    'lonely': f'{BASE_URL}/videos/lonely.mp4'
}

@app.route('/')
def homepage():
    # Seleciona um vídeo aleatório
    random_video = random.choice(list(videos.values()))
    return render_template('index.html', background=random_video)

if __name__ == '__main__':
    app.run(debug=True)
