import web

# URLs de la aplicación ubicadas en controllers 
urls = (
    '/', 'mvc.controllers.index.Index',
)

app = web.application(urls, globals())
session = web.session.Session(app, web.session.DiskStore('sessions'))

if __name__ == "__main__":
    web.config.debug = True
    app.run()

