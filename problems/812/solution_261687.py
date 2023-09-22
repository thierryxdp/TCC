def retira_pontuacao(texto):
    """Dado um texto qualquer, retira a pontuação e substituí por espaço:
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
        return texto