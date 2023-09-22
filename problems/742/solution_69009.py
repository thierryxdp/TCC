def substitui(s,x,i):
    '''
    funcao que retorna a primeira str dada,visto que
    a questao nos da: string,int,int->string
    '''
    subs=s[0:i]+str(x)+s[i+1:]
    return subs