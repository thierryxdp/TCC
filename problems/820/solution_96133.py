def posLetra(frase,letra,ocorrencia):
"""retorna em que posi ̧c~ao da string a ocorr^encia desejada da letra est ́a.
str,str,int -> int"""
    pos = 0
    contador = 0
    while pos < len(frase):
             if frase[pos] == letra:
                 contador = contador + 1
                 if contador == ocorrencia:
                     return pos
             pos = pos + 1
    return -1