def posLetra(texto,letra,num):
    """Essa funçao retorna a posição de uma letra em uma string,
    dado a string, a letra e qual o numero da ocorrencia
    str,str,int->"""
    
    i = 0
    j = 0
    
    while i < len(texto):
        
        if texto[i] == letra: #verifica se a letra da posicao e a letra desejada
            j += 1
            if j == num: #verifica se a quantidade de ocorrencias da letra e igual a pedida
                return i
        i+=1
            
    return -1