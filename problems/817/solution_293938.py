'''Função querecebe uma lista com as notas dos alunos e retornam
	aquela que esteja bem velhinha ja.
    list -> int.'''
def acima_da_media(lista):
    nota=sum(lista)/len(lista)
    if nota not in lista:
        lista.append(nota)
        list.sort(lista)
        posicao=list.index(lista,nota)+1
        return lista[posicao:]
    else:
        list.sort(lista)
        posicao=list.index(lista,nota)+1
        return lista[posicao:]