import web

render = web.template.render("templates/views/")

class Index():

    def GET(self):
        try:
            return render.index()
        except Exception as e:
            return "ERROR " + str(e.args)