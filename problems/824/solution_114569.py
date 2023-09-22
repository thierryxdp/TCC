def uppCons(frase):
    '''Funcao que, dada uma frase, retorna a mesma frase com todas as consoantes em maiúsculo; str -> str'''
    frase=str.split(frase)
    proxima=0
    str.upper(proxima)=maiusculo
    while proxima<len(frase):
        if frase[proxima] not in "aeiouAEIOU":
            novalista=str.replace(frase,proxima,maiusculo)
    proxima=proxima+1
    return join(novalista)