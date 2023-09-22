def retira_pontuacao(frase):
    """Dada uma frase, essa função retorna essa frase sem todos os caracteres de pontuação
    str-->str"""
    frase=str.replace(frase,"-"," ")
    frase=str.replace(frase,","," ")
    frase=str.replace(frase,":"," ")
    frase=str.replace(frase,";"," ")
    frase=str.replace(frase,"?"," ")
    frase=str.replace(frase,"!"," ")
    frase=str.replace(frase,"."," ")
    return frase