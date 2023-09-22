import math
def acima_da_media(lista_notas):
    media = int(math.floor(sum(lista_notas)/len(lista_notas)))
    if media in lista_notas:
        list.append(lista_notas, media)
        list.sort(lista_notas)
        ocorrencia = list.index(lista_notas, media)
        return lista_notas[ocorrencia+2:]
    else:
        list.append(lista_notas, media)
        list.sort(lista_notas)
        ocorrencia = list.index(lista_notas, media)
        return lista_notas[ocorrencia+1:]
#Nesse execicio utilizei o mais do mesmo q venho aprendo
#Strings como sort e append
#Len para contabilizar o numero d caracteres