def retira_pontuacao(frase):
    """xxx"""
    
    pontuacao = ['-',',',':',';','.']
    
    frase = map(frase.replace(x,' '),pontuacao)
    
    return frase