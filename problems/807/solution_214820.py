def conta_frases(texto):
    '''Retorna quantas frases aparecem
       no texto inserido; str->int'''
    mod1=str.replace(texto,'.','#')
    mod2=str.replace(mod1,'...','#')
    mod3=str.replace(mod2,'!','#')
    mod4=str.replace(mod3,'?','#')
    count=str.count(mod4,'',-1,len(lista)//2)
    lista=str.split(mod4,'#')
    listaf=len(lista)
    return listaf-count