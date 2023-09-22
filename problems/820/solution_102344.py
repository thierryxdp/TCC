def posLetra(frase,letra,num):
    '''Recebe como entrada uma palavra ou frase, uma letra e a ocorrência 
    da letra na palavra ou frase, retornando em que posição a ocorrência
    letra está na palavra ou frase.
    str, str, int -> int'''
    ocorr=0
    posicao=0
    while (ocorr<=num)and(posicao<len(frase)):
        posicao=frase.find(letra,posicao)
        if posicao!=-1:
            ocorr=ocorr+1
            posicao=posicao+1
    return posicao-1