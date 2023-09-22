def remover_pontuacao(frase):
    """xxx"""
    
    return frase.replace(x,' ')


def retira_pontuacao(frase):
    """xxx"""
    
    pontuacao = ['-',',',':',';','.']
    
    frase = map(remover_pontuacao,pontuacao)
    
    return frase