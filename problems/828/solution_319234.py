def primo(numero):
    contador_1=0
    contador_2=0
    raiz=math.floor(math.sqrt(numero))
    while contador_1 < raiz:
        contador_1 += 1
        divisao = numero/(contador_1)
        if divisao == round(divisao):
            contador_2 += 1
    return(contador_2==1)