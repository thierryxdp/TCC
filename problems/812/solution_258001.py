def retira_pontuacao(frase):
    """Função que, dada uma frase retira todos os caracteres de pontuação e os substirui por espaço
    str->str"""
    s = frase
    return s.replace(s.replace(".")," ")