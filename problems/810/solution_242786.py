def retira_pontuacao(frase):
    NF = frase[:]
    for simbolos in ["-",",",":",";",".","?","!"]:
        NF=str.replace(NF,simbolos," ")
        for simbolos in [",",":",";",".","?","!"]:
            NF=str.replace(NF,simbolos," ")
            for simbolos in [":",";",".","?","!"]:
                NF=str.replace(NF,simbolos," ")
                for simbolos in [";",".","?","!"]:
                    NF=str.replace(NF,simbolos," ")
                    for simbolos in [".","?","!"]:
                        NF=str.replace(NF,simbolos," ")
                        for simbolos in ["?","!"]:
                            NF=str.replace(NF,simbolos," ")
                            for simbolos in ["!"]:
                                NF=str.replace(NF,simbolos," ")
                                return NF
def inverte(frase):
    ''' Função que recebe uma string "frase", e retorna uma string
    contendo os elementos da string original, porém com as palavras
    na ordem inversa'''
        #casos de teste:
    ''' inverte("Jájá eu termino o MT")
    ->  'MT o termino eu Jájá'
        inverte("Socorram-me subi no onibus em Marrocos")
        'Marrocos em onibus no subi Socorram-me'
        inverte("Achei que daria certo o ex anterior")
        'anterior ex o certo daria que Achei' '''
    NF=retira_pontuacao(frase)
    Fm=str.lower(NF)
    Fs=str.split(Fm)
    list.reverse(Fs)
    Li=Fs
    Fi=str.join(" ", Li)
    return Fi