def posLetra(frase,letra,ocorr):
    '''recebe como entrada uma string, uma letra, e um número que 
indica a ocorrência desejada da letra (1 para primeira ocorrência, 
2 para segunda, etc). retornando em que posição da string aquela
ocorrência da letra está. Caso exista menos ocorrências 
da letra do que a ocorrência pedida, a função retornará -1'''
    vezes=0
    indice=0
    while indice<len(frase):
        if vezes<ocorr:
            if frase[indice]==letra:
                vezes+=1
            indice+=1
    if vezes<ocorr:
        return -1
    return indice