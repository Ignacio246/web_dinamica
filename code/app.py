import web

urls = (
    '/', 'templates.mvc.index.Index',
    '/webpy', 'templates.mvc.web.Webpy',
    '/javascript', 'templates.mvc.javascript.Javascript',
)
app = web.application(urls, globals())


if __name__ == "__main__":
    app.run()