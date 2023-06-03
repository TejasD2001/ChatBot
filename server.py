from flask import Flask, send_from_directory, url_for
import subprocess

app = Flask(__name__, static_folder='static')


@app.route('/')
def index():
    return '''
        <html>
            <head>
                <meta charset="UTF-8">
                <meta http-equiv="X-UA-Compatible" content="IE=edge">
                <meta name="viewport" content="width=device-width, initial-scale=1.0">
                <title>MedBot</title>
                <link rel="stylesheet" href="{{ url_for('static', filename='C:/Users/tejas/OneDriveD/esktop/MEGA PROJECT/Project/Aura/static/style.css') }}">


                <link rel="icon" type="image/x-icon" href="C:/Users/tejas/OneDrive/Desktop/MEGA PROJECT/Project/Aura/Images/Icon/apple-touch-icon.png">
                <style>
                    body {background-image: url("C:/Users/tejas/OneDrive/Desktop/MEGA PROJECT/Project/Aura/Images/Wallpaper/Wallpaper 3.jpg");
                    background-position: 50%;
                    background-repeat: no-repeat;}
                    h1   {color: blue;}
                    p    {color: red;}
                </style>
            </head>
            <body>
                <h1>Run Python</h1>
                <button onclick="runPython()">Click me to run Aura</button>
                <script>
                function runPython() {
                const xhr = new XMLHttpRequest();
                xhr.open('GET', '/run-python');
                xhr.send();
                }
                </script>
            </body>
        </html>
    '''


@app.route('/static/style.css')
def css():
    return send_from_directory('static', 'style.css')


@app.route('/run-python')
def run_python():
    output = subprocess.check_output(['python', 'app.py'])
    return output


if __name__ == '__main__':
    app.run()
