def repetidos(lista):
    '''funcao qie recebe a lista de números e retorna o número de ocorrências que determinado número aparece nessa lista;
    list -> int'''
    a = 0
    b = len(lista)
    while a < b:
        if lista[a] == list[a-1]:
            a = a + 1
    return a