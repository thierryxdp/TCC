def retira_pontuacao(frase):
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