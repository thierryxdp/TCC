""""Retorna as notas acima da média:
int->int"""
def maiores(inteiro,n):
    inteiro=inteiro
    list.append(inteiro,n)
    list.sort(inteiro)
    retorna=list.index(inteiro,n)
    return inteiro[retorna+1:]
def acima_da_media(lista):
    list.sort(lista)
    media=sum(lista)/len(lista)
    list.append(lista, media)
    volta=list.index(lista,media)
    return volta