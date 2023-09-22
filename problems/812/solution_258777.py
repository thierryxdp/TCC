def retira_pontuacao(frase):
    """Função que substitui  os caracteres de pontuação por espaço
    str->str"""
    return frase.replace(".", " ").replace("!"," ").replace("-"," ").replace(":"," ").replace(";"," ").replace("?"," ").replace(","," ")