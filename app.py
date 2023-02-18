from paquetes.models import Cliente

# 4 Atributos (nombre, apellido, edad, email)

cliente = Cliente("Florencia", "Aguirre", 30, "floraguirre1598@gmail.com")
cliente1 = Cliente("Juan","Perez",28,"juan@juan.com")
cliente2 = Cliente("Pedro","Fernandez",25,"pedro@pedro.com")
cliente3 = Cliente("Sandra","Aguirre",50,"sandra@sandra.com")


# Metodo 1 = getInfo

print(cliente.getInfo())
print(cliente1.getInfo())
print(cliente2.getInfo())
print(cliente3.getInfo())

# Metodo 2 = getEdad

print(cliente.getEdad())
print(cliente1.getEdad())
print(cliente2.getEdad())
print(cliente3.getEdad())

# Metodo 3 = getEmail

print(cliente.getEmail())
print(cliente1.getEmail())
print(cliente2.getEmail())
print(cliente3.getEmail())