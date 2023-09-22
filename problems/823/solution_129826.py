def faltante(lista):
    list.sort(lista)
    tamanho=len(lista)
    todas=list(range(lista[0],tamanho+2))
    elementoemlista=0
    elementoemtodas=0

    while elementoemlista<len(lista):
        if lista[elementoemlista]==todas[elementoemtodas]:
            elementoemlista=elementoemlista+1
            elementoemtodas=elementoemtodas+1
        else:
            return todas[elementoemtodas]+1