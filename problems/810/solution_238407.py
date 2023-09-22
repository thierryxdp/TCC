def retira_pontuacao(frase):
    """Função que ao receber uma frase(str), retorna essa mesma frase,
    mas sem os caracteres de pontuação, que são substituídos por espeço;
    str -> str"""
    frasef = str.replace(str.replace(str.replace(str.replace(str.replace(frase, ',', ' '), '!',' '),'.',' '), '?', ' '),'-', ' ')
    return frasef
def inverte(frase):
    frasef1 = str.split(frase, ' ')
    frasef2 = str.join('', frasef1[::-1])
    frasef3 = str.join('', frasef2[::1])
    return str.lower(retira_pontuacao(frasef3))