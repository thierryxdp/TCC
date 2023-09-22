def retira_pontuacao(f):
    """dada uma frase, retorna a frase com todos os caracteres de pontuação substituídos por espaço
(str --> str) """
    k = str.replace(f,"."," ")
    k = str.replace(k,"?"," ")
    k = str.replace(k,":"," ")
    k = str.replace(k,"-"," ")
    k = str.replace(k,"!"," ")
    k = str.replace(k,";"," ")
    k = str.replace(k,"..."," ")
    k = str.replace(k,","," ")
    return k