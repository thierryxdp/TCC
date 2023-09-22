def retira_pontuacao(x):
    '''
    Função que retira todas as pontuações de uma frase, dada como entrada. 
    Os caracteres de pontuação são substituidos por espaço.
    str->str
    '''
    y=str.replace(x,'-',' ')
    z=str.replace(y,',',' ') 
    w=str.replace(z,':',' ')
    n=str.replace(w,';',' ')
    k=str.replace(n,'.',' ')
    c=str.replace(k,'?',' ')
    v=str.replace(c,'!',' ')
    
    return v