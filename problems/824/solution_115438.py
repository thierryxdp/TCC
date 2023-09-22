def uppCons(f):
    '''Essa função ao receber como valor de entrada um frase, retorna a frase com todas as suas consoantes em maiúsculas'''
    ''' str -> str'''
    i = 0
    resposta = ''
    
    while i < len (f):
        texto=frase[i]
        if texto in 'b,c,d,f,g,h,j,k,l,m,n,p,q,r,s,t,v,wx,y,z,ç':
            texto = str.upper(texto)
        resposta = resposta + texto 
        i = i + 1
    return resposta