def uppCons(frase):
    '''Retorna a frase inserida com todas as suas consoantes maiúsculas; str->str'''
    indice=0
    fraseM=''
    while indice<len(frase):
        if frase[indice] not in 'ÃÕÂÊÎÔÛÁÉÍÓÚAEIOUaeiouáéíóúâêîôûãõ':
            letra=str.upper(frase[indice])
            fraseM=fraseM+letra
        else:
            fraseM=fraseM+frase[indice]
        indice=indice+1
    return fraseM