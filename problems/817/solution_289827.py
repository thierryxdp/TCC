def acima_da_media (lista):
    """Função que recebe uma lista com as notas dos alunos e retorna as notas que ficaram acima da media; lista -> lista"""
    x = sum(lista)
    y = len(lista)
    media = x/y
    maiores=[]
    for i in lista:
        if i >= media:
            maiores.append(i)
            return media, maiores