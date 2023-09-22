def acima_da_media(notas):
    """

list -> list
acima_da_media([1,2,3,4,5,6,7,8,9,10]) == []
acima_da_media([]) == []
"""
    media = (sum(notas))/len(notas)
    list.sort(notas)
    return notas[list.index(notas,media):]