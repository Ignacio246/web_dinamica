import web

render = web.template.render("templates/views/")

class Javascript():

    def GET(self):
        resultado = 0
        try:
            return render.javascript(resultado)
        except Exception as e:
            return "ERROR " + str(e.args)