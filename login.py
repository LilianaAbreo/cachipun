def login():
    username = input("ingrese su nombre: ")
    password = input("ingrese su contraseña: ")

    if username == "admin" and password == "12345":
        print(f"Ingreso exitoso y bienvenido {username} ")
        return True
    else:
        print("usario o contraseña incorrecto")
        return False

if __name__  == "__main__":
    login()
