import web 

class ModeloIndex:
    def __init__(self):
        pass

    def consulta(self, username, password):
        try:
            if username == "usuario" and password == "1234":
                return "Valido"
            else:
                return "Invalido"
        except Exception as e:
            print(f"Error en modelo{e}")
            return None
 


    
