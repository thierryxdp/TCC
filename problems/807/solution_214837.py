def conta_frases(texto):
    '''Retorna quantas frases aparecem
       no texto inserido; str->int'''
    mod1=str.replace(texto,'...','#')
    mod2=str.replace(mod1,'!','#')
    mod3=str.replace(mod2,'?','#')
    count=str.count(mod3,'.')
    lista=str.split(mod3,'#')
    listaf=len(lista)
    return listaf-count