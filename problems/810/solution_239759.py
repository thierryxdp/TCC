def inverte(frase):
    '''funcao que recebe uma frase, e devolve ela invertida sem letras maiusculas ou pontuaçao;str-->str'''
    frase=str.split(frase)
    x=str.lower(frase)
    x=str.replace(frase,'.',' ')
    y=str.replace(x,',',' ')
    z=str.replace(y,':',' ')
    u=str.replace(z,'-',' ')
    s=str.replace(u,';',' ')
    p=str.replace(s,'!',' ')
    q=str.replace(p,'?',' ')
    
    o=q[::-1]
    i=str.join('',q)
    return i