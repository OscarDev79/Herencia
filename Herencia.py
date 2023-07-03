# Autor Oscar Albarracin
# Crear una clase Persona con las siguientes variables:

# La edad, El nombre ,El teléfono

# Una vez creada la clase, crea una nueva clase Cliente que herede de Persona, esta nueva clase tendrá la variable credito solo para esa clase.

# Crear ahora un objeto de la clase Cliente que debe tener como propiedades la edad, el telefono, el nombre y el credito, tienes que darles valor y mostrarlas por pantalla.

# Una vez hecho esto, haz lo mismo con la clase Trabajador que herede de Persona, y con una variable salario que solo tenga la clase Trabajador.

class Persona:
    def __init__(self, edad, telefono, nombre):
        self.edad = edad
        self.telefono = telefono
        self.nombre = nombre

class Cliente:
    def __init__(self, credito, edad, telefono, nombre):
        Persona.__init__(self, edad, telefono, nombre)
        self.credito = credito

El_cliente = Cliente(15210 ,25, 632051924, 'Ania')
print('El cliente se llama: ' + El_cliente.nombre + ' tiene: ' + str(El_cliente.edad) + ' años y su telf es: ' + str(El_cliente.telefono) + ' y tiene un credito de: ' +str( El_cliente.credito))

class Trabajador:
    def __init__(self, salario, edad, telefono, nombre):
        Persona.__init__(self, edad, telefono, nombre)
        self.salario = salario

El_trabajador = Trabajador(1450, 32, 726541824, 'Jose')
print('Hola me llamo: ' + El_trabajador.nombre + ' tengo: ' + str(El_trabajador.edad) + ' años y mi movil es: ' + str(El_trabajador.telefono) + ' y este es mi salario: ' + str(El_trabajador.salario))