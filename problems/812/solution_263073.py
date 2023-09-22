def retira_pontuacao(frase):
    """dada uma frase a funcao retorna a frase com todos os 
    caracteres substituidos por espacos; str->str"""
    frase1=str.join(" ", str.split(frase, '-'))
    frase2=str.join(" ", str.split(frase1, ','))
    frase3=str.join(" ", str.split(frase2, ':'))
    frase4=str.join(" ", str.split(frase3, ';'))
    frase5=str.join(" ", str.split(frase4, '...'))
    frase6=str.join(" ", str.split(frase5, '?'))
    frase7=str.join(" ", str.split(frase6, '!'))
    frase8=str.join(" ", str.split(frase7, '.'))
    return frase8