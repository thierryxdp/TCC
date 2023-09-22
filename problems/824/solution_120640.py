def uppCons(frase):
    """ Recebe uma frase e retorna a mesma, porém com suas 
    consoantes em maiúsculo"""
    R = 0
    proximo = 0 
    while  proximo < len(frase):
        if e in ['q','w','r','t','y','p','s','d','f','g','h','j','k','l','z','x','c','v','b','n','m']:
            R = R + str.replace(frase,e,str.upper(e))        
    return R