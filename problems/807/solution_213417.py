def conta_frases(texto):
    '''fucao que retorna a contagem do numero de frases, sendo cada 
    str->int'''
    subst1= str.replace(texto,'...','!')
    subst2= str.replace(subst1,'.','!')
    subst3= str.replace(subst2,'?','!')
    contagem= str.count(subst3,'!')
    
    return contagem