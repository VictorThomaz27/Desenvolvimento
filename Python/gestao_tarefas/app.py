from flask import Flask, request, redirect, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return 'Bem-vindo ao aplicativo de gestão de tarefas!'

if __name__ == '__main__':
    app.run(debug=True)
    # Lista global de tarefas
    tarefas = []
    proximo_id = 1

    def adicionar_tarefa(texto):
        global tarefas, proximo_id
        tarefa = {
            'id': proximo_id,
            'texto': texto,
            'completa': False
        }
        tarefas.append(tarefa)
        proximo_id += 1
        return tarefa

    def completar_tarefa(id):
        global tarefas
        for tarefa in tarefas:
            if tarefa['id'] == id:
                tarefa['completa'] = True
                return True
        return False
