def acima_da_media(lista):
    """Retorna uma lista ordenada com as notas que ficaram
    	acima da média"""
    l_final = []
    for i in lista:
        media = sum(lista)/len(lista)
        if i > media:
            l_final.append(i)
            
    l_final.sort()
           
    return l_final