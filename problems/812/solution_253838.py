def retira_pontuacao(frase):
    """Dada uma frase, essa função retorna essa frase sem todos os caracteres de pontuação
    str-->str"""
    str.replace(frase,"-"," ")
    str.replace(frase,","," ")
    str.replace(frase,":"," ")
    str.replace(frase,";"," ")
    str.strip(frase,"?")
    str.strip(frase,"!")
    str.strip(frase,".")
    return frase