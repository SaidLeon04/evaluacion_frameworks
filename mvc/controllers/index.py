import web
from mvc.model.modelo_index import ModeloIndex

render = web.template.render('mvc/views/')

m_index = ModeloIndex() # Instancia de la clase ModeloIndex

class Index:
    def GET(self):
        try:
            return render.index(username=None, password=None, resultado=None)
        except Exception as e:
            print(f"Error 101 - index(){e.args}")
            return "mal"
        
    def POST(self):
        try:
            form = web.input()
            username = form.username
            password = form.password
            resultado = m_index.consulta(username, password)
            if resultado == "Valido":
                web.setcookie("username", username, expires="", domain=None, secure=False)
                return render.pagina(username)
            else:
                return render.index(username=None, password=None, resultado=None)
            
        except Exception as e:
            print(f"Error 102 - index(){e.args}")
            return "mal"
            