def filtra_pares(tupla):
    tupla_nova = ()
    if tupla[0] %2==0:
        tupla_nova = tupla_nova+(tupla[0],)
    if tupla[1] %2==0:
        tupla_nova = tupla_nova+(tupla[1],)
    if tupla[2] %2==0:
        tupla_nova = tupla_nova+(tupla[2],)
    if tupla[3] %2==0:
        tupla_nova = tupla_nova+(tupla[3],)
    return tupla_nova


def tipos(tupla):
    lista_string = []
    lista_resto = []
    
    if type(tupla[0]) != bool:
        if type(tupla[0]) == str:
            lista_string = [tupla[0],]
        else:
            lista_resto = [tupla[0],]
            
    if type(tupla[1]) != bool:
        if type(tupla[1]) == str:
            lista_string = [tupla[1],]
        else:
            lista_resto = [tupla[1],]
        
    if type(tupla[2]) != bool:
        if type(tupla[2]) == str:
            lista_string = [tupla[2],]
        else:
            lista_resto = [tupla[2],]
    return lista_string, lista_resto