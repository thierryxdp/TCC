def uppCons(frase):
    '''Função que recebe uma frase e retorna 
    a frase com todas as suas consoantes em 
    maiúsculas e os demais caracteres como 
    estavam na frase de entrada. 
    Dados de entrada: str
    Valor de saída: str
    '''
    verificacao_vogais = 'AEIOUaeiouÂâÊêÎîÔôÛûÁáÉéÍíÓóÚúÀàÈèÌìÒòÙùÃãÕõ'
    indice_frase = 0 
    frase_alterada = ''
    while indice_frase < len(frase):
        if frase[indice_frase] not in verificacao_vogais:
            letra_maiúscula = frase[indice_frase].upper()
            frase_alterada = frase_alterada + letra_maiúscula
        else: 
            frase_alterada = frase_alterada + frase[indice_frase]
        indice_frase = indice_frase + 1
    return frase_alterada