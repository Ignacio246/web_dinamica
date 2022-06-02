import web

urls = (
    '/', 'templates.mvc.index.Index',
    '/docker', 'templates.mvc.docker.Docker',
    '/ubuntu', 'templates.mvc.ubuntu.Ubuntu',
)
app = web.application(urls, globals())


if __name__ == "__main__":
    app.run()