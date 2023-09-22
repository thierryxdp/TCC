def uppCons(frase):
    '''Funcao que, dada uma frase, retorna a mesma frase com todas as consoantes em maiúsculo; str -> str'''
    frase=str.split(frase)
    proxima=0
    while proxima<len(frase):
        if frase[proxima] not in "aeiouAEIOU":
            str.upper(proxima)=maiusculo
            novalista=str.replace(frase,proxima,maiusculo)
    proxima=proxima+1
    return join(novalista)