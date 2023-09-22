def posLetra(frase,letra,ocorrencia):
    '''função que recebe uma string, uma letra e um número
    que indica a ocorrência desejada da letra e retorna em
    que posição da string aquela ocorrência está.
    
    str, str, int -> int'''
    
    i=0
    posicao = []
    
   
    if len(frase) >= ocorrencia: 
        while i<len(frase):
            if letra in frase[i]:
                list.append(posicao,i)
            i=i+1
        return posicao[ocorrencia-1]
    elif len(frase)<ocorrencia:
        return -1