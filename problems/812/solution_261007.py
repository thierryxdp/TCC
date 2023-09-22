def retira_pontuacao(frase):
    ''' Função que recebe uma string "frase" de entrada,
    e retorna a mesma string substituindo os caracteres especiais
    ("-", "," , ":", ";", ".") por um espaço'''
    '''str -> str'''
    #casos de teste:
    ''' retira_pontuacao('Eu-estou, demorando a terminar: meu deus.')
    -> 'Eu estou  demorando a terminar  meu deus '
        retira_pontuacao('provas; provas; preciso estudar mais.')
    -> 'provas  provas  preciso estudar mais '
        retira_pontuacao('ele disse -quimica é facil, brincou.')
    -> 'ele disse  quimica é facil  brincou ' '''
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