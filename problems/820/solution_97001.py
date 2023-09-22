def posLetra (frase, letra, num):
    '''função que recebe uma string, uma letra e um número e retorna
    a posição da string aquela ocorrência está
    tipo de entrada: str, str, int
    tipo de saída: int'''
    
    posicao= frase.find(letra)
        
        while posicao >= 0 and num > 1:
            posicao = frase.find(letra, posicao +1)
            num -= 1
            
        return posicao