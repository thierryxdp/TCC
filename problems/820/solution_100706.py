def posLetra(string,letra,numero):
    
    '''Função que recebe uma string e retorna a posição da n-ésima ocorrência de uma letra de entrada nessa string. str,str,int -> int'''
    
    i = 0
    k = 0
    
    while (i < len(string)) and (numero != k):
        if letra in string[i]:
            k = k + 1
        i = i + 1
        
    return (i - 1)