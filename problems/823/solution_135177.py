def faltante(lista):
    '''Função que consegue identificar qua peça 
    está faltando no quebra-cabeça
    entrada=list
    saida=int'''
    lista1=sorted(lista)
    i=0
    while i<len(lista1):
        if i+1!= lista1[i]:
            return i +1
        i=i+1
    return len(lista1)+1