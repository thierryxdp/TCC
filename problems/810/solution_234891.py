def inverte(tuple):
    """Para inverter a frase desejada, digite;
    str->str"""
   
    lista1 = list(range(tuple[0],tuple[10]))
        
    lista2 = lista1[-2::-1]
    return lista2