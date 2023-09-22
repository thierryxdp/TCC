def uppCons(frase):
    """Retorna a frase recebida com todas as suas consoantes maiúsculas"""
    
    consoantes = ['q','w','r','t','y','u','p','s','d','f','g','h','j','k','l','ç','z','x','c','v','b','n','m']
    
    frase = str(map(replace(consoantes,consoantes[i].upper),frase))
    
    return frase