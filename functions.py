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