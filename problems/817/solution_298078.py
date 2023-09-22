def acima_da_media(lista):
    """Dada uma lista de notas de um aluno calcula a sua média e retorna as notas que estão
	list -> list"""
    media = sum(lista) / len(lista)
    lista.append(media)
    listaorg = sorted(lista)
    indmedia = listaorg.index(media)
    novalista = listaorg[indmedia +1:]
    if media in novaLista:
    	del novaLista[0]

    return novaLista