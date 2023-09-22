def freq_palavras(frases):
    '''
    Funçao que recebe uma frase e retorna um dicionario que 
    diz quantas vezes as palavras sao repetidas na frase
    str -> dict
    '''
    dicio=[]   
    lista = frases.split(" ")
    for i in range(len(lista)):        
        palavra= lista[i]
        x=list.count(lista, palavra)
        list.append(dicio,palavra)       
        list.append(dicio,x)       
        i=i+1
    dict(dicio)
    return dicio