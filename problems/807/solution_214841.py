def conta_frases(texto):
    '''Retorna quantas frases aparecem
       no texto inserido; str->int'''
    mod1=str.count(texto,'.')
    mod3=str.replace(texto,'!','#')
    mod4=str.replace(mod3,'?','#')
    lista=str.split(mod4,'#')
    listaf=len(lista)
    return listaf-mod1