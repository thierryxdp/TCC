def retira_pontuacao(frase):
    '''retorna a frase onde todos os caracteres de ointuação são substituídos por 
    espaço.
    str -> str'''
    
    pontuacao = ('!',',','.',';',':','?','-')
    
    if pontucao in frase:
        retun str.replace(frase, str(pontuacao), ' ')