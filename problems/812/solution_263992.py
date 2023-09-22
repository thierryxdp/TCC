def retira_pontuacao (q):
    '''Função que tira pontuação de travessão, virgula, dois pontos, ponto e virgula e ponto final seja substituido
    por espaço.
    str -> str'''
    
    a = str.replace (q,'-',',')
    b = str.replace (a,',',':')
    c = str.replace (b,':',';')
    d = str.replace (c,';','...')
    e = str.replace (d,'...','.')
    reutnr str. replace (e,'.',' ')