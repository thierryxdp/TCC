def colchao(lista,altura_porta,largura_porta):
    espessura = lista[0] 
    largura = lista[1]  
    altura = lista[2] 
    if espessura < largura_porta and altura < altura_porta:
        return True
    if larura < largura_porta and espessura < altura_porta:
        return True 
    if espessura < largura_porta and largura < altura_porta:
        return True
    else:
        return False