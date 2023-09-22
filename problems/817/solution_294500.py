def maiores(lista,n):
    if n not in lista:
        lista.append(n)
        lista.sort()
        a = lista.index(n)
        lista_numeros = lista[a+1:]
        rep = lista_numeros.count(n)
        return lista_numeros[rep:]
    
   def acima_da_media(lista_notas):
        '''Função que dada como entrada uma lista com as 
        notas dos alunos retorne outra função, com apenas as
        notas acimas da média. list --> list.'''
        medias = sum(lista_notas)/len(lista_notas)
        return maiores(lista_notas,medias)