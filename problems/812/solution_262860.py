def retira_pontuacao(frase):
    """Função que substitui toda a pontuação de uma frase por espaço"""
    """string->string"""
    if "," in frase:
        frase_nova=str.replace(frase,","," ")
        elif "." in frase:
            frase_nova=str.replace(frase,"."," ")
    return frase_nova