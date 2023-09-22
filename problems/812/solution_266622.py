def retira_pontuacao(frase):
    """ retorna a frase onde todos os caracteres de pontuação tenham sido substituídos por espaço str-->str"""
    str.replace(frase,","," ")
    str.replace(frase,"."," ")
    str.replace(frase,":"," ")
    str.replace(frase,"-"," ")
    str.replace(frase,";"," ")
    str.replace(frase,"!"," ")
    str.replace(frase,"?"," ")