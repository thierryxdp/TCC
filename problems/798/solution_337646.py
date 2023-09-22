def freq_palavras(frases):
    '''
    Funçao que recebe uma frase e retorna um dicionario que 
    diz quantas vezes as palavras sao repetidas na frase
    str -> dict
    '''
    x=1
    dicio={}
    lista = frases.split(" ")
    for i in range(len(lista)):
        for j in range(len(lista)):
            if j == i:
                x=x+1
                dicio=dict.append(j,x)
            	j=j+1
            else:
                j=j+1