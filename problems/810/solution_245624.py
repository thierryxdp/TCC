def retira_pontuacao(texto):
    """Dado um texto, retorna o texto sem as pontuações:
    str-->str"""
    pontos=['!','?','.','-',':',';',',','...']
    for pontos in pontos:
        texto=texto.replace('!',' ')
        texto=texto.replace('?',' ')
        texto=texto.replace('.',' ')
        texto=texto.replace('-',' ')
        texto=texto.replace(':',' ')
        texto=texto.replace(';',' ')
        texto=texto.replace(',',' ')
        texto=texto.replace('...',' ')
        texto=texto.lower()
        return texto

def inverte(texto):
    """Dado um texto, retorna o texto sem pontuação, sem letras maiúscula
    e invertido:
    str-->str"""
    texto=retira_pontuacao(texto)
    texto=texto.split(' ')
    inverso=' '.join(reversed(texto)) 
    return inverso