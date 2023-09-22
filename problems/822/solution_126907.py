def repetidos(a):
    'recebe uma lista e retorna o numero de vezes que o elemento anterior é repetido'
    'entrada: list'
    'saida: int'
    i=0
    repeticao=0
    while 1+i<len(a):     
        if a[i]==a[1+i]:        
            repeticao+= 1 
        i= i+1
    return repeticao