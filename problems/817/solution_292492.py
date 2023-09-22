def acima_da_media(lista):
    """Função que retorna a média das notas, e quais ficaram acima da média"""
    media = sum(lista)//len(lista)
    lista.sort()
    return list((sum(lista)/len(lista),sub_lista(lista,media)))