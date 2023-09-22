def acima_da_media (lista_notas):
    """Recebe uma lista com as notas dos alunos de uma turma,
    e retorna a lista apenas com os valores acima da média.
    list -> list"""
    media = sum(lista_notas)/len(lista_notas)
    
    if media not in lista_notas:
        list.append (lista_notas, media)
        list.sort (lista_notas)
        comeco = list.index(lista_notas, media) + 1
        return lista_notas[comeco:] 
    
    else:
        list.sort (lista_notas)
        comeco2 = list.index(lista_notas, media) + 1
        return lista_notas[comeco2:]