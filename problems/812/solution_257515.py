def retira_pontuacao(frase):
    """xxx"""
    
    return frase.replace(x,' ')
   
    pontuacao = ['-',',',':',';','.']
    
    frase = map(retira_pontuacao,pontuacao)
    
    return frase