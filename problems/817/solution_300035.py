def acima_da_media(lista_de_notas):
    """Funçao que faz a media das notas dos alunos"""
    "list-->list"
    media = 5
    list.sort(lista_de_notas)
    if 5 in lista_de_notas :
        A=list.index(lista_de_notas, 5)
        list.sort(lista_de_notas)
        return lista_de_notas[A: ]