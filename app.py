from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'PBonjour je rencontre bcp de probleme pour deployer avec ArgoCD'