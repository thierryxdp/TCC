def lingua_p(texto):
    """ Recebe uma palavra e reorna a plavara traduzida para 
    lingua do P. str-->str"""
    p=''
    lista=[]
    vogais=['a','e','i','o','u','á','é','í','ó','ú','A','E','I','O','U','Á','É','Í','Ó','Ú']
    for elemento in texto:
        if elemento in vogais:
            list.append(lista,str(elemento)+"p"+str(elemento))
        else:
            list.append(lista,str(elemento))
    for var in range(len(lista)):
        p=p+lista[var]
    return p.lower()