from flask import Flask, render_template, request, Markup


app = Flask(__name__, template_folder="./src/views")

@app.route("/", methods=["GET", "POST"])
def home():
    if (request.method == "GET"):
        return render_template("index.html")
    else:
        if (request.form["num1"] != "" and request.form["num2"] != ""):
            if (request.form["operacao"] == "soma"):
                soma = int(request.form["num1"]) + int(request.form["num2"])
                return Markup('<div class="bg-dark p-5" style="height: 100vh"> <div class="container border p-4 bg-white"> <h4>O resultado da operação é: <h4>') + str(soma) + Markup('<link href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1" crossorigin="anonymous"> </br></br> <a href="/"><button class="btn btn-primary">Voltar</button></a>')
            elif (request.form["operacao"] == "subtracao"):
                subtracao = int(request.form["num1"]) - int(request.form["num2"])
                return Markup('<div class="bg-dark p-5" style="height: 100vh"> <div class="container border p-4 bg-white"> <h4>O resultado da operação é: <h4>') + str(subtracao) + Markup('<link href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1" crossorigin="anonymous"> </br></br> <a href="/"><button class="btn btn-primary">Voltar</button></a>')
            elif (request.form["operacao"] == "multiplicacao"):
                multiplicacao = int(request.form["num1"]) * int(request.form["num2"])                 
                return Markup('<div class="bg-dark p-5" style="height: 100vh"> <div class="container border p-4 bg-white"> <h4>O resultado da operação é: <h4>') + str(multiplicacao) + Markup('<link href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1" crossorigin="anonymous"> </br></br> <a href="/"><button class="btn btn-primary">Voltar</button></a>')
            else:
                divisao = int(request.form["num1"]) // int(request.form["num2"])
                return Markup('<div class="bg-dark p-5" style="height: 100vh"> <div class="container border p-4 bg-white"> <h4>O resultado da operação é: <h4>') + str(divisao) + Markup('<link href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1" crossorigin="anonymous"> </br></br> <a href="/"><button class="btn btn-primary">Voltar</button></a></div></div>')                
        else:            
            return Markup('<div class="bg-dark p-5" style="height: 100vh"> <div class="container border p-4 bg-white"> <h4>Por favor, informar ambos os números</h4>') + Markup('<link href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1" crossorigin="anonymous"> </br> <a href="/"><button class="btn btn-primary">Voltar</button></a>')
                
            
app.run(port=5000, debug=True)