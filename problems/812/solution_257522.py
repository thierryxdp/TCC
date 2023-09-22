def retira_pontuacao(frase):
    """Mostra a frase fornecida sem pontuações"""
    
    pontuacoes = ['...','!','?','.',',','-']
    nova = map(frase,pontuacoes)
    
    return nova