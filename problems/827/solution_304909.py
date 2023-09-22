def qtd_divisores(numero):
    contagem=0
    for item in range(1,numero+1):
        if numero%item ==0:
            contagem+=1
    return contagem