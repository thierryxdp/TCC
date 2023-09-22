def qtd_divisores(numero):
    contagem=0
    possibilidades = range(1,numero+1)
    for item in possibilidades:
        if numero%item ==0:
            contagem+=1
    return contagem