def retira_pontuacao(frase):
    '''Funcao que dada uma frase, retorna a frase com todos os
    caracteres de pontuacao substituidos por espaco
    str -> str'''
    travessao = str.replace(frase,"-", " ")
    virgula = str.replace(frase,",", " ")
    doispontos = str.replace(frase,":", " ")
    pontovirgula = str.replace(frase,";", " ")
    pontofinal = str.replace(frase,".", " ")
    return travessao + virgula + doispontos + pontovirgula + pontofinal