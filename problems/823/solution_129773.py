def faltante(lista):
    '''Função retorna a peça faltante de um quebra-cabeça;
    list -> int'''
    i=1
    while i<=len(lista):
        if i not in lista:
            return i
        if lista[-1]<len(lista)+1:
            return lista[-1] + 1
        i+=1