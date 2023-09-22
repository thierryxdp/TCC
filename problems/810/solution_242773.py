def inverte(frase):
    ''' funçao que recebe uma string "frase" de entrada,
    e retorna uma string contendo a mesma string, porém com as palavras
    em ordem invertida'''
    ''' str -> str '''
    #casos de teste:
    ''' inverte("Jájá eu termino o MT")
    ->  'MT o termino eu Jájá'
        inverte("Socorram-me subi no onibus em Marrocos")
        'Marrocos em onibus no subi Socorram-me'
        inverte("Achei que daria certo o ex anterior")
        'anterior ex o certo daria que Achei' '''
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
                        NF=str.split(frase)
                        NF.reverse()
                        frase=str.join(" ", NF)
                        return frase