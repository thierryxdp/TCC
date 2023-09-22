def retira_pontuacao(frase):
    '''retorna a frase onde todos os caracteres de ointuação são substituídos por 
    espaço.
    str -> str'''
    
    pontuacao = ('!',',','.',';',':','?','-')
    
    if str(pontuacao) in frase:
        return str.replace(frase,pontuacao, ' ')