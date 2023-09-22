""""Retorna as notas acima da média:
int->int"""
def acima_da_media(lista):
    variante=[l for l in lista if l>(sum(lista)/len(lista))]
    list.sort(variante)
    return variante