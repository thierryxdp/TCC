def retira_pontuacao(frase):
    '''Função que retorna a frase com todos seus caracteres de pontuação substituídos por espaço
    string -> string'''
    frase = str.replace(frase,".", " ")
    frase = str.replace(frase,",", " ")
    frase = str.replace(frase,":", " ")
    frase = str.replace (frase,"-"," ")
    frase = str.replace(frase,";"," ")
    frase = str.replace(frase,"!"," ")
    frase = str.replace(frase,"?"," ")

    return frase