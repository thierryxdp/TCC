def faltante(lista_num):
    '''Encontra o número da peça faltando em um quebra-cabeças, list -> int'''
    i = 1
    while i < len(lista_num):
        if 1 not in lista_num:
            return 1
        elif lista_num[i-1] + 1 == lista_num[i]:
            i = i + 1
        elif lista_num[i-1] + 1 != lista_num[i]:
            return lista_num[i] + 1
        else:
            return lista_num[len(lista_num)-1]+1