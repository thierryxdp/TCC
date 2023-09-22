def posLetra(frase,letra,n):
    '''
    Função que recebe uma string (frase), uma letra (letra)
    e um numero de ocorrencia (n) desejada da letra nesta frase.
    retorna a posição da string em que a letra está
    str, str, int -> int
    '''
    contador = 0
    frase2 = ""
    
    while contador < n-1:       
        if frase.count(letra) == n:
            return frase.rfind(letra)
        elif frase.count(letra) != n:
            frase.replace(letra,"&",(n-1)) 
        return frase.find(letra)