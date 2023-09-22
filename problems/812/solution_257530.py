def retira_pontuacao(frase):
    """Mostra a frase fornecida sem pontuações"""
    
    pontuacoes = ['...','!','?','.',',','-']
    espaco = ' '
    nova = str(map(str.replace(frase),espaco,pontuacoes))
    
    return nova