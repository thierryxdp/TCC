def primo(numero):
    lista = []
    for x in range(1,numero+1):
        divisao = numero%x
        if divisao == 0:
            lista.append(x)
    if len(lista)>2:
        return False
    else:
        return True