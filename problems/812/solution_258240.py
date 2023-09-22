def retira_pontuacao(frase):
    """Função que dada uma 'frase', retorna essa frase com os caracteres de pontuação substituídos
    por espaço; str -> str"""

    termo1 = str.replace(frase,"-"," ")
    termo2 = str.replace(termo1,":"," ")
    termo3 = str.replace(termo2,";"," ")
    termo4 = str.replace(termo3,"?"," ")
    termo5 = str.replace(termo4,"!"," ")
    termo6 = str.replace(termo5,","," ")
    termo7 = str.replace(termo6,"."," ")
    
    return termo7