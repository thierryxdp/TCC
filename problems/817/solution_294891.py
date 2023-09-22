def acima_da_media(lista):
    """Função que retorna uma lista de notas acima da media apartir da lista de notas dos alunos
    lis -> list"""
    x = (sum(lista))/(len(lista))
    maiores_que_n =  [numero for numero in lista if numero > x]
    list.sort(maiores_que_n)
    return maiores_que_n