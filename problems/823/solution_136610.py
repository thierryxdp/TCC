def faltante(lista_num):
    '''Encontra o número da peça faltando em um quebra-cabeças, list -> int'''
    i=0
    while i<len(lista_num):
        if lista_num[i]+1==lista_num[i+1]:
            i=i+1
        else:
            return lista_num[i]+1