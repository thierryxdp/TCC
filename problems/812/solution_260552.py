def retira_pontuacao(frase):
    '''
    Função que dada uma frase retorna a frase onde todos os caracteres de
    pontuação são substituídos por espaço.
    
    str-> str
    '''
    a=frase.replace('-','  ')
    b=a.replace(',','  ')
    c=b.replace(':','  ')
    d=c.replace(';','  ')
    e=d.replace('!','  ')
    f=e.replace('?',' ')
    g=f.replace('.','  ')
    return f.replace