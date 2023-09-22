def repetidos(lista):
    '''funcao qie recebe a lista de números e retorna o número de ocorrências que determinado número aparece nessa lista;
    list -> int'''
    x = 0
    while x < len(lista):
        if x in lista:
            list.count(lista,x)
        x = x + 1
    return x