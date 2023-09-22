def retira_pontuacao(frase):
    """Mostra a frase fornecida sem pontuações"""
    
    pontuacoes = ['...','!','?','.',',','-']
    espaco = ' '
    nova = list(map(espaco,frase,['...','!','?','.',',','-']))
    
    return nova