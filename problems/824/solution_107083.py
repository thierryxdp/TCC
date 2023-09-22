def uppCons ( frase ): 
    """ funcao ira receber uma frase e ira retornar essa mesma frase porem com todas as consoantes em letra maiuscula
    entrada : string      saida: string"""
    i = 0
    novafrase = ''
    while i < len (frase):
        if frase [i] not in 'AEIOUaeiouÃãÁáÂâÉéÊêÍíÕõÓóÔôÛûÚú':
            novafrase = novafrase + (str.upper (frase[i]))
        elif frase [i] in 'AEIOUaeiouÃãÁáÂâÉéÊêÍíÕõÓóÔôÛûÚú':
            novafrase = novafrase + frase[i]
        i = i + 1
    return novafrase