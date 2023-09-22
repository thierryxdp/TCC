def retira_pontuacao(frase):
    """Retira todas as pontuaçõesda frase, substituindo elas por espaço
       retornando a frase modificada
       str --> str"""
    frase.replace(frase,"!"," ")
    str.replace(frase,"."," ")
    str.replace(frase,":"," ")
    str.replace(frase,"?"," ")
    str.replace(frase,";"," ")
    str.replace(frase,","," ")
    return