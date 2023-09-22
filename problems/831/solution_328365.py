def lingua_p(texto):
    """ Recebe uma palavra e reorna a plavara traduzida para 
    	lingua do P. str-->str"""
    p=''
    lista=[]
    vogais=['a','e','i','o','u','á','é','í','ó','ú','A','E','I','O','U','Á','É','Í','Ó','Ú']
    for var in texto:
        if var in vogais:
            list.append(lista,str(var)+"p"+str(var))
        else:
            list.append(lista,str(var))
    for k in range(len(lista)):
        p=p+lista[k]
    return p.lower()