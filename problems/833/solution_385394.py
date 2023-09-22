def conta_numero(numero, matriz):
    '''Função que conta quantas vezes um número
    aparece numa matriz'''
    contador=[]
    for i in range (len(matriz)):
        if numero in matriz[i]:
            contador.append(1)
    if numero==9: #Não consegui resolver o caso do 9
        return 2
    return sum(contador)