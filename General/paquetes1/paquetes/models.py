

class Cliente:


    def __init__(self,nombre,apellido,edad,email):
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad
        self.email = email

      

    def setNombre(self, nombre):
        self.nombre = nombre

    def getNombre(self):
        return self.nombre

    def setApellido(self, apellido):
        self.apellido = apellido

    def getApellido(self):
        return self.apellido

    def setEdad(self, edad):
        self.edad = edad

    def getEdad(self):
        return self.edad

    def setEmail(self, email):
        self.email = email

    def getEmail(self):
        return self.email

    def getInfo(self):
        
        info = "\n---- Informacion del Cliente -----\n"
        info += "\n Nombre: " +  self.getNombre()
        info += "\n Apellido: " + self.getApellido()
        info += "\n Edad: " + str(self.getEdad())
        info += "\n Email: " + str(self.getEmail())
        

        return info




# Utilización de __str__
    def __str__(self):
        texto = "Se ha registrado el usuario {0}"
        return texto.format(self.nombre)