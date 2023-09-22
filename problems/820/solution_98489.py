def posLetra (frase,letra,ocorrencia):
    '''Dado uma frase, uma letra contida na frase a um numero
    que indica a ocorrencia desejada da letra, retorna a posição
    na frase em que a ocorrencia da letra se encontra;
    str,str,int->int'''
    aparicao= 0
    posicao_aparicao=0
    while aparicao != ocorrencia:
        if letra in frase:
            posicao_aparicao= str.find(frase,letra,posicao_aparicao+1)
        aparicao+=1
    
    return posicao_aparicao