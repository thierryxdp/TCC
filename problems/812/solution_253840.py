def retira_pontuacao(frase):
    """Dada uma frase, essa função retorna essa frase sem todos os caracteres de pontuação
    str-->str"""
    frase_nova=str.replace(frase,"-"," ")
    frase_nova=str.replace(frase_nova,","," ")
    frase_nova=str.replace(frase_nova,":"," ")
    frase_nova=str.replace(frase_nova,";"," ")
    frase_nova=str.strip(frase_nova,"?")
    frase_nova=str.strip(frase_nova,"!")
    frase_nova=str.strip(frase_nova,".")
    return frase_nova