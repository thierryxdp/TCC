def uppCons(frase):
    """Retorna a frase recebida com todas as suas consoantes maiúsculas"""
    
    consoantes = ['q','w','r','t','y','u','p','s','d','f','g','h','j','k','l','ç','z','x','c','v','b','n','m']
    consupp = ['Q','W','E','R','T','Y','P','S','D','F','G','H','J','K','L','Ç','Z','X','C','V','B','N','M']
    
    frase = str(map(str.replace(consoantes,consupp),frase))
    
    return frase