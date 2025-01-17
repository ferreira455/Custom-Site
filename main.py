from flask import Flask, render_template, request
import random

app = Flask(__name__)

# Lista de vídeos na pasta 'static/videos'
videos = {
    'alone': 'https://www.dropbox.com/scl/fi/3pz0uc7bmuyweqzwoz8db/alone.mp4?rlkey=9ep5rckl38iumdj5q6n4hrbof&st=l8nz76i8&dl=1',
    'girl': 'https://www.dropbox.com/scl/fi/ldepsfh5rx5wqykkddt54/girl.mp4?rlkey=kp1pln0p6l4hk2hgjrayy5ftg&st=thb3gekb&dl=1',
    'girl sleeping': 'https://www.dropbox.com/scl/fi/04mmc0b4zt1m8hx4ekzus/girl-sleeping.mp4?rlkey=80kd6rxb0rmlkz1z0bnws9ez0&st=843wux3u&dl=1',
    'mountain': 'https://www.dropbox.com/scl/fi/qhfsobt08bopedrbsz0hb/mountain.mp4?rlkey=ekpnai2csloj62oazcpi2m77d&st=diyii4td&dl=1',
    'solo leveling': 'https://www.dropbox.com/scl/fi/5jqzlytpd6ke1aitq0q5l/solo-leveling.mp4?rlkey=1ctxuwg9tmgh8ig0n0dwemii6&st=qx8315m8&dl=1',
    'lonely': 'https://www.dropbox.com/scl/fi/tde6nap57qhol4q5poxlt/lonely.mp4?rlkey=0op5m2s16wmsmw4uo48adpycj&st=izvz4ja5&dl=1'
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
