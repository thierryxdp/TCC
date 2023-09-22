def faltante (lista_inteiros):
    '''
    função que dada uma lista de inteiros, retorna o número que falta dentro na lista num intervalo de 1 a N
    (dado que falta apenas uma peça/numero)
    list--->int
    '''
    i = 1
    resposta=0

    while i < len(lista_inteiros):
        if ((lista_inteiros[i-1])+1)!= lista_inteiros[i]:
            resposta= resposta+lista_inteiros[i-1]+1
      
        elif ((lista_inteiros[0]!= 1)):
            resposta= 1
        else:
            resposta= resposta+ 0
        
        i=i+1

    return resposta