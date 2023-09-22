def retira_pontuacao(frase):
    """Função que ao receber uma frase(str), retorna essa mesma frase,
    mas sem os caracteres de pontuação, que são substituídos por espeço;
    str -> str"""
    frasef = str.replace(str.replace(str.replace(str.replace(str.replace(frase, ',', ' '), '!',' '),'.',' '), '?', ' '),'-', ' ')
    return frasef
def inverte(frase):
    frasef = str.split(frase, ' ')
    frasef= str.join(' ', frase)
    return frasef