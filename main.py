from flask import Flask, render_template
import random

app = Flask(__name__)

# Lista de imagens
images = {
    'alone': 'https://cdn.imgchest.com/files/4z9cveqxmv7.png',
    'aot': 'https://cdn.imgchest.com/files/4gdcxd3r8d4.jpg',
    'girl playing': 'https://cdn.imgchest.com/files/y8xcnea89x4.png',
    'girl sleeping': 'https://cdn.imgchest.com/files/45xcv6awnm7.png',
    'mountain': 'https://cdn.imgchest.com/files/4apc569ond4.png',
    'solo leveling': 'https://cdn.imgchest.com/files/46acqnle987.png'
}

@app.route('/')
def homepage():
    # Seleciona uma imagem aleatória
    random_image = random.choice(list(images.values()))
    return render_template('index.html', background_image=random_image)

if __name__ == '__main__':
    app.run(debug=True)
