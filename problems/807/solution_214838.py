def conta_frases(texto):
    '''Retorna quantas frases aparecem
       no texto inserido; str->int'''
    mod2=str.replace(texto,'!','#')
    mod3=str.replace(mod2,'?','#')
    count=str.count(mod3,'.')
    lista=str.split(mod3,'#')
    listaf=len(lista)
    return listaf-count