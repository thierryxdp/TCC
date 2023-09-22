def posLetra(frase,letra,n):
    'dada uma string e uma letra retorne a posição do n no qual é o numero de ocorrencia desejada.str,str,int-->int'
    posicao=str.find(frase,letra)
    pos_antes=posicao
    i=0
    while i<len(frase):
        if posicao<n:
        pos_antes=posicao
        posicao=str.find(frase,letra,posicao+1)
        i=i+1
        else:
            -1
        
    return posicao