def acima_da_media (notas):
    """Função que, dada uma lista com as notas dos alunos, retorna uma lista ordenada com as notas acima da média
    Entrada: lista[int]
    Saída: lista[int]"""
    
    soma_das_notas = sum(notas)
    quantidade_de_notas = len(notas)
    media = soma_das_notas / quantidade_de_notas
    list.sort(notas)
    return media