def posLetra(string,l,n):
    '''Recebe como entrada uma string, uma letra, e um número indicando a ocorrência da letra. Retorna em que posição da frase aquela ocorrência se encontra.
str,str,int -> int'''
    x = 0
    for y in range(len(string)): 
        if (string[y] == l): 
            x += 1  
  
        if (x == n): 
            return y