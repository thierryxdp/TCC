def retira_pontuacao(frase):
    """Função que dada uma frase, substitui os caracteres de pontuação por espaço;
    str -> str"""
    if '!':
        return str.replace(frase,"!"," ")
    if '?':
        return str.replace(frase,"?"," ")
    if '.':
        return str.replace(frase,"."," ")
    else:
        if '-':
            return str.replace(frase,"-"," ")
        else ',':
            return str.replace(frase,","," ")