def retira_pontuacao(frase):
    '''
    Função que dada uma frase retorna a frase onde todos os caracteres de
    pontuação são substituídos por espaço.
    
    str-> str
    '''
    a=str.replace(frase,'-','  ',)
    b=a.replace(a,',','  ',)
    c=b.replace(b,':','  ', )
    d=c.replace(c,';','  ', )
    e=d.replace(d,'!','  ', )
    f=e.replace(e,'?',' ', )
    g=f.replace(f,'.','  ', )
    return frase.replace