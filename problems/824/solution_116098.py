def uppCons(frase):
    "função que recebe uma frase (str) e retorna outra frase (str)com as consoantes maiúsculas"
    posicao = 0
    while posicao < len(frase):
        if not frase[posicao] in [a,e,i,o,u]:
            str.replace(frase,frase[posicao],str.upper(frase[posicao]))
        posicao +=1
    return frase