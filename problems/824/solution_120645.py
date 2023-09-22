def uppCons(frase):
    """ Recebe uma frase e retorna a mesma, porém com suas 
    consoantes em maiúsculo""" 
    for e in frase:
        if e in ['ç','q','w','r','t','y','p','s','d','f','g','h','j','k','l','z','x','c','v','b','n','m']:
            frase =  str.replace(frase,e,str.upper(e))        
    return frase