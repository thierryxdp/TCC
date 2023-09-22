def acima_da_media(notas):
    """recebe conjunto listado com n e retorna novo conjunto em ordem crescente
    entrada: list, int
    saida: list"""
    soma=sum(notas)
    l=len(notas)
    media=soma//l
    if len(notas)>=2:
        list.append(notas,media)
        list.sort(notas)
        objeto=list.index(notas,media)
        notas=notas[objeto+1:]
        return notas
    
    else:
        return []