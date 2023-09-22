def acima_da_media(lista):
    '''função que, dada uma lista com as notas dos alunos, retorne as notas
    acima da média.
    list -> list'''
    listanova = []
    soma_notas = sum(lista)
    quantos_alunos = len(lista)
    media = soma_notas/quantos_alunos
    
    for n in lista:
        if n <= media:
            remove(n)
            return lista