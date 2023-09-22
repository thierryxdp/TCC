def acima_da_media(lista):
    media = sum(lista)/len(lista)
    notasmedia = list.insert(lista, media, 0)
    ordenados = list.sort(lista)
    return lista[notasmedia:]