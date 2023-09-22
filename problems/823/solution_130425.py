def faltante(N):
    '''Dada uma lista N, descubra qual número está faltando na sequência; list-> int'''
    ocorrencia=1
    list.sort(lista)
    while ocorrencia in lista:
        ocorrencia=ocorrencia+1
    return ocorrencia