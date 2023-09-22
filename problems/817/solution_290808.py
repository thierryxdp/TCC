def acima_da_media(lista):
    """essa"""
    media = sum(lista)/len(lista)
    maior = sum( i > media for i in lista )
   	return maior