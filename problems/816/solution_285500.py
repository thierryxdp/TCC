def maior_que(elemento,valor_limite):
    if(elemento > valor_limite):
        return True
    else:
        return False
    return False
def maiores(lista,n):
    resultado = filter(lambda n: maior_que(elemento,n),lista)
    return resultado