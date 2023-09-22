def retira_pontuacao(frase):
    '''Função que ao receber uma frase, a retorna substituindo os
    	caracteres de pontuação por espaço
        
        str -> str'''
    x=frase.replace('-',' ')
    y=x.replace(',',' ')
    z=y.replace(':',' ')
    w=z.replace(';',' ')
    v=w.replace('.',' ')
    u=v.replace('!',' ')
    a=u.replace('?',' ')
    b=a.replace('...',' ')
    return b