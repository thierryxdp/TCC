def acima_da_media(notas):
    '''retorna as notas que ficaram acima da média'''
   if 5 in notas:
        notas.sort()
        ind=lista.index(5)
        return lista.index[ind:]
    else:
        lista.insert(0,5)
        lista.sort()
        ind=lista.index(5)
        return lista[ind+1:]