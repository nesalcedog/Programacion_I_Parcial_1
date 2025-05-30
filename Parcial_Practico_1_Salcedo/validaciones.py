def es_entero(valor):
    
    if type(valor) == str and valor.isdigit():
        return True
    print('Error: Ingrese un numero entero')
    return False

def es_flotante(valor):
    if type(valor) == float:
        return True
    
    if type(valor) == str and "." in valor:
        partes = valor.split(".")
        return partes[0].isdigit() and partes[1].isdigit()
    return False

def es_digito(valor):
    if type(valor) == str and  valor.isdigit():
        return True
    print('Error: Ingrese un digito')
    return False

    
    