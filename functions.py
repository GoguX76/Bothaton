#Función que valida que el usuario haya ingresado bien el nombre.
def validacionUsuario(nom):
    try:
        if not nom.strip(): #Con esto, compruebo que no hayan espacios ni caracteres dentro del nombre.
            raise ValueError("El campo de nombre no puede estar vacío.")
        
        if not nom.strip().isalpha(): #Con esto, compruebo que no hayan caracteres ni espacios, pero también que no haya números.
            raise ValueError("El nombre no puede contener números.")
        
        if len(nom) < 4: #Con esto, compruebo que la longitud del nombre sea mayor a 4 caracteres.
            raise ValueError("El nombre debe tener 4 carácteres como mínimo.")
        return True
    
    #En los excepts se manejan y muestran los errores definidos en los if de arriba.
    except TypeError as e:
        print(f"Error: {e}")
        return False
    except ValueError as e:
        print(f"Error: {e}")
        return False

#Función que le pide al usuario ingresar su nombre y luego validarlo con validacionUsuario().   
def obtenerUsuario():
    while True:
        nom = input(">> ").capitalize()
        if validacionUsuario(nom):
            return nom
        
#Función que valida que el usuario haya ingresado bien la edad.
def validacionEdad(age):
    try:
        if not age.strip():
            raise ValueError("El campo de edad no puede estar vacío.")
        
        if any(c.isalpha() for c in age):
            raise ValueError("La edad no puede contener letras.")
        
        age_int = int(age)

        if age_int <= 0:
            raise ValueError("La edad no puede ser un numero negativo.")
        
        if age_int > 120:
            raise ValueError("La edad no puede ser mayor a 120 años.")
        
        return True
        
    except ValueError as e:
        print(f"Error: {e}")
        return False
    
def obtenerEdad():
    while True:
        age = input(">> ")
        if validacionEdad(age):
            return age

def validacionGenero(gender):
    try:
        if not gender.strip():
            raise ValueError("El campo de genero no puede estar vacío.")
        
        if not gender.strip().isalpha():
            raise ValueError("El genero no puede tener números.")
        
        if len(gender) > 1:
            raise ValueError("El genero solo puede tener un caracter (M/F).")
        
        if gender not in ["M", "F"]:
            raise ValueError("Ha ingresado un valor erroneo.")
        
        return True
    except ValueError as e:
        print(f"Error: {e}")
        return False
    except TypeError as e:
        print(f"Error: {e}")
        return False
    
def obtenerGenero():
    while True:
        gender = input(">> ").upper()

        if validacionGenero(gender):
            if gender == "M":
                gender = "Masculino"
                return gender
            else:
                gender = "Femenino"
                return gender
            
def almacenarDatos():
    print("Para empezar, ingrese su nombre")
    nom = obtenerUsuario()

    print("Ahora, ingrese su edad")
    age = obtenerEdad()

    print("Por último, ingrese su genero")
    gender = obtenerGenero()

    datosUsuarios = {
        "Nombre": nom,
        "Edad": age,
        "Genero": gender
    }

    return datosUsuarios

def registrarUsuarios():
    users = []

    while True:
        print("=== Registro de Usuarios ===")
        data = almacenarDatos()
        users.append(data)

        registrar = input("¿Quiere ingresar a otro usuario? (S/N): ").upper()
        if registrar != "S":
            break
    
    return users

def mostrarUsuarios(users):
    if not users:
        print("No se han encontrado usuarios en el sistema")
        return
    
    print("=== USUARIOS REGISTRADOS ===")
    for i, user in enumerate(users, 1):
        print(f"Usuario {i}")
        print(f"Nombre: {user["Nombre"]}")
        print(f"Edad: {user["Edad"]}")
        print(f"Genero: {user["Genero"]}")
    print(f"Total de Usuarios: {len(users)}")