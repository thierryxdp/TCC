def acima_da_media(lista):
    """retorna a média das notas e os quais estão acima da média"""
    acima_da_media = sum(lista)//len(lista)
    lista.sort()
    return list((sum(lista)/len(lista),sub_lista(lista,acima_da_media)))