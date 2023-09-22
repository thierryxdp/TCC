def acima_da_media(notas):
    '''Função que dada uma lista com as notas dos alunos de uma turma, retorna
uma lista ordenada com as notas que ficaram acima da média.
    list -> list
    '''
    media = sum(notas)/len(notas)
    resposta = maiores(notas,media)
    return resposta