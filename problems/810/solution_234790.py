def retira_pontuacao2(frase):
    ''' Ao ser dada como entrada uma frase (string, entre aspas simples ou du-
    plas), a funcao retorna uma nova string com todas as pontuacoes removidas,
    (inclusive travessao, virgula, dois pontos, ponto e virgula e todas as pon-
    tuacoes de comeco e fim de frase), substituindo-as por espaco; 
    
    str -> str '''
    
    frase = frase.replace('!','*')
    frase = frase.replace('?','*')
    frase = frase.replace('...','*')
    frase = frase.replace('.','*')
    frase = frase.replace(',','*')
    frase = frase.replace(':','*')
    frase = frase.replace(';','*')
    frase = frase.replace('-','*')
    
    frase_final = frase.replace('*',' ')
    
    return frase_final

def inverte(frase):
    ''' Dada uma frase como entrada, a funcao inverte a ordem de suas palavras, 
    alem de remover as pontuacoes e colocar todas em letra minuscula; 
    
    str -> str ''' 
    
    
    frase = retira_pontuacao2(frase)
    frase = str.lower(frase)
    frase = frase.split(' ')
    frase = frase[::-1]
    frase = str.join(' ',frase)
    
    return frase