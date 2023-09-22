def acima_da_media(lista):
    
    '''A função retornará as notas dos alunos que obtiveram grau superior a média
    da turma.
    
    dados de entrada -> lista
    dados de saída -. lista'''
    
    Q = len(lista)
    Soma = sum(lista)
    Media = Soma/Q
    Maiores = maiores(lista,Media)
	
    if Media in Maiores:
        return Maiores
    
    else:
	return Maiores

media = int(sum(lista) / len(lista))
    lista.append(media)
    listaOrganizada = sorted(lista)
    indiceMedia = listaOrganizada.index(media)
    novaLista = listaOrganizada[indiceMedia + 1:].copy()
return novaLista


print(acima_da_media([7, 0, 8, 2, 4, 9, 5, 3])) # [5, 7, 8, 9]
print(acima_da_media([0, 2, 6, 9])) #[6,9]
print(acima_da_media([8, 9, 7])) # [9]