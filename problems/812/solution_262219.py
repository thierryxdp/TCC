def retira_pontuacao(frase):
    '''retorna uma frase sem as pontuacoes'''
    '''str -> str'''
    
    f=frase.replace('.','')
    f=frase.replace('/','')
    f=frase.replace(';','')
    f=frase.replace(',','')
    f=frase.replace(':','')
    f=frase.replace('-','')
    f=frase.replace('?','')
    f=frase.replace('!','')
    
    return f