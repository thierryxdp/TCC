def uppCons(frase):
    '''A função recebe uma frase e retorna outra frase com todas as consoantes da frase
    original em maiúsculas e com os demais caracteres exatamente como estavam.
    Parâmetro de entrada: str
    Valor de retorno: str'''
    i=0
    frase_nova=frase
    while i<len(frase):
        if frase[i] in "BCÇDFGHJKLMNPQRSTVWXYZbcçdfghjklmnpqrstvwxyz":
            consoante_maiscula=str.upper(frase[i])
            frase_nova=str.replace(frase_nova,frase[i],consoante_maiscula)
        i=i+1
    return frase_nova