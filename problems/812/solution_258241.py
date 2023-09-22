def retira_pontuacao(frase):
    '''Funcao que dada uma frase, retorna a frase com todos os
    caracteres de pontuacao substituidos por espaco
    str -> str'''
    v1 = str.replace(frase,"-", " ")
    v2 = str.replace(v1,",", " ")
    v3 = str.replace(v2,":", " ")
    v4 = str.replace(v3,";", " ")
    v5 = str.replace(v4,".", " ")
    v6 = str.replace(v5,"!", " ")
    v7 = str.replace(v6,"?", " ")
    return v7