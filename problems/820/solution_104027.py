def posLetra(frase, letra, numero):
    '''Recebe uma string (frase), uma letra
    (letra) e um número (numero) e retorna a
    posição da letra na ocorrência desejada
    
    str, str, int -> int
    '''
    palavras = list(frase)
    
    contador = 0
    ocorrencias = 0
    
    while len(palavras) > contador:
        
        if letra in palavras[contador]:
            ocorrencias += 1
            
            if ocorrencias == numero:
                return contador
        contador +=1
    if ocorrencias < numero:
        return -1
    else:
        return ocorrencias