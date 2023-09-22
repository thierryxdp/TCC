def posLetra(texto,letra,numero):
    '''função que recebe como entrada uma string "texto" e retorna a 
    posição(índice) da string em que a string "letra" aparece em sua
    ocorrência de valor "numero", caso o número de ocorrências seja menor
    do a entrada "numero", a função retorna -1; string,string,int->int'''
    
    i=0
    n=0
    
    while i<len(texto) and n<numero:
        if letra == texto[i]:
            n=n+1
        i=i+1
    if n<numero:
        return -1
    
    return i-1