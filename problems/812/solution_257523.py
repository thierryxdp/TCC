def retira_pontuacao(frase):
    """Mostra a frase fornecida sem pontuações"""
    
    pontuacoes = ['...','!','?','.',',','-']
    nova = list(map(frase,pontuacoes))
    
    return nova