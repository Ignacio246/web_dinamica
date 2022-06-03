import web

render = web.template.render("templates/views/")

class Webpy():

    def GET(self):
        resultado = 0
        try:
            return render.webpy(resultado)
        except Exception as e:
            return "ERROR " + str(e.args)
    
    def POST(self):
        form = web.input()
        num1 = int(form.num1)
        num2 = int(form.num2)
        resultado = num1 + num2
        return render.webpy(resultado)