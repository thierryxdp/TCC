def freq_palavras(frases):
    '''
    Funçao que recebe uma frase e retorna um dicionario que 
    diz quantas vezes as palavras sao repetidas na frase
    str -> dict
    '''    
   	
    lista = frases.split(" ")
    for i in range(len(lista)):
        palavra= lista[i]
        x=list.count(lista, palavra)
        dicio=dicio[palavra].append(x)
        i=i+1
    return dicio