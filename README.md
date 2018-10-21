
# PYTHON WEBSOCKET WITH FLASK

Projet de Rolf pour un enregistreur à bandes STUDER a810 24
https://mpe.berklee.edu/documents/studio/manuals/multitrack/Studer%20A810/Studer%20A810.pdf



https://projects.raspberrypi.org/en/projects/python-web-server-with-flask/3

https://flask-socketio.readthedocs.io/en/latest/

https://github.com/miguelgrinberg/Flask-SocketIO

https://ouilogique.com/installer-raspian-stretch/

https://alex.dzyoba.com/blog/python-import/


    sudo apt-get --assume-yes update
    sudo apt-get --assume-yes dist-upgrade
    sudo apt-get install python3-flask
    sudo pip3 install --upgrade pip3
    sudo pip3 install Flask-SocketIO eventlet pyyaml

    mkdir webapp && cd webapp

    mkdir templates && cd templates
    nano index.html

```
<html>
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no" />
<link rel="stylesheet" href="/static/bootstrap.min.css" />
</head>
<body>
<h1>Hello from a template!</h1>
</body>
</html>
```

    nano name.html

```
<html>
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no" />
<link rel="stylesheet" href="/static/bootstrap.min.css" />
</head>
<body>
<h1>Hello {{ name }}!</h1>
</body>
</html>
```

    cd ..
    nano app.py
copy + paste following code

```
#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/cakes')
def cakes():
    return 'Yummy cakes!'

@app.route('/hello/<name>')
def hello(name):
    return render_template('name.html', name=name)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
```

Run app

    python3 app.py



---

    sudo pip install --upgrade pip

    pip install Flask-SocketIO

    conda create --name rpi_websocket_conda
    source activate rpi_websocket_conda
    conda install -c anaconda flask
    sudo conda install -c conda-forge flask-socketio
    sudo conda install -c anaconda flask-socketio
    export FLASK_APP=test_websocket.py

    conda install -c conda-forge eventlet
    conda install -c anaconda pyyaml

eventlet pyyaml




