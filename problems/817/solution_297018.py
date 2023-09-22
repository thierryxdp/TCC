def acima_da_media(lista):
    """Função que recebe uma lista com as notas dos alunos de uma
    turma e retorna uma lista, em ordem crescente, com as notas que 
    ficaram acima da média.
    list->list
    """
    calculo_media= sum(lista)/len(lista)
    return maiores (lista, calculo_media)