def maior_que(elemento,valor_limite):
    if(elemento > valor_limite):
        return True
    else:
        return False
    return False
def maiores(lista,n):
    resultado = sort(lista)
    resultado = filter(lambda elemento: maior_que(elemento,n),lista)
    return list(resultado)