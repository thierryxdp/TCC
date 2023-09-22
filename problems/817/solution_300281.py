def acima_da_media(lista):
    """
        Dada uma lista de notas de um aluno calcula a sua média
        e retorna as notas que estão acima da média.
        list -> list
    
        Parâmentros:
        Entrada: lista = lista de notas
        Retorna: Lista no modelo
        [Média, notas maiores que a média organizadas do menor pro maior]
    """
    
    media = int(sum(lista)/len(lista))
    lista.append(media)
    lista.sort()
    novaLista = lista[lista.index(media)+1:]
    
    if media in novaLista:
        return novaLista

    elif media not in novaLista:
        novaLista.insert(0,media)
        return novaLista