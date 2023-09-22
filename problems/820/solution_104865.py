def posLetra(frase,referente,indice):
    '''Função que recebe como entrada uma string, uma letra
    e um numero que indica a ocorrencia desejada da letra e
    retorna em que posição da string aquela ocorrencia da letra;
    str, str, int -> int'''
    i = 0
    s = []
    while i < len(frase):
        if  frase[i]==referente:
            s = s + [i]
            if (len(s)+1)<=indice:
                r = -1
            if (len(s)+1)>indice:
                r = s[indice-1]
        i = i + 1
    return r