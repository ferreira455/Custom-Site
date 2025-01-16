from flask import Flask, render_template
import random

app = Flask(__name__)

# Lista de vídeos na pasta 'static/videos'
videos = {
    'alone': 'videos/alone.mp4',
    'girl playing': 'videos/girl.mp4',
    'girl sleeping': 'videos/girl-sleeping.mp4',
    'mountain': 'videos/mountain.mp4',
    'solo leveling': 'videos/solo-leveling.mp4',
    'lonely': 'videos/lonely.mp4'
}

@app.route('/')
def homepage():
    # Seleciona um vídeo aleatório
    random_video = random.choice(list(videos.values()))
    return render_template('index.html', background=random_video)

if __name__ == '__main__':
    app.run(debug=True)
