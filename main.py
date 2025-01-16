from flask import Flask, render_template, request
import random

app = Flask(__name__)

# Lista de vídeos na pasta 'static/videos'
videos = {
    'alone': 'static/videos/alone.mp4',
    'girl playing': 'static/videos/girl.mp4',
    'girl sleeping': 'static/videos/girl-sleeping.mp4',
    'mountain': 'static/videos/mountain.mp4',
    'solo leveling': 'static/videos/solo-leveling.mp4',
    'lonely': 'static/videos/lonely.mp4'
}

@app.route('/')
def homepage():
    # Seleciona um vídeo aleatório
    random_video = random.choice(list(videos.values()))
    
    # Obtém a URL onde a aplicação está rodando
    app_url = request.url_root
    
    # Cria a URL completa do arquivo de vídeo
    video_url = app_url + random_video

    # Exibe as URLs
    print(f"A aplicação está rodando em: {app_url}")
    print(f"A URL do vídeo 'alone.mp4' é: {app_url}static/videos/alone.mp4")

    # Retorna o template com o vídeo aleatório
    return render_template('index.html', background=random_video)

if __name__ == '__main__':
    app.run(debug=True)
