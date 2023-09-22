def retira_pontuacao(frase):
    NF = frase[:]
    for simbolos in ["-",",",":",";","."]:
        NF=str.replace(NF,simbolos," ")
        for simbolos in [",",":",";","."]:
            NF=str.replace(NF,simbolos," ")
            for simbolos in [":",";","."]:
                NF=str.replace(NF,simbolos," ")
                for simbolos in [";","."]:
                    NF=str.replace(NF,simbolos," ")
                    for simbolos in ["."]:
                        NF=str.replace(NF,simbolos," ")
                        return NF
def inverte(frase):
    ''' Função que recebe uma string "frase", e retorna uma string
    contendo os elementos da string original, porém com as palavras
    na ordem inversa'''
    NF=NL
    NL=str.split(frase)
    NL.reverse()
    frase=str.join(" ", lista)
    return frase