def retira_pontuacao(frase):
    """xxx"""
    
    pontuacao = ['-',',',':',';','.']
    
    frase = map(frase.replace(pontuacao,' '),pontuacao)
    
    return frase