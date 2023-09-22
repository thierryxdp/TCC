def faltante(N):
    '''Dada uma lista N, descubra qual número está faltando na sequência; list-> int'''
    ocorrencia=1
    list.sort(N)
    while ocorrencia in N:
        ocorrencia=ocorrencia+1
    return ocorrencia