def m(lista, numero):
    """Funcao que dada uma lista de numeros inteiros e um numero inteiro retorna outra lista
    que contem todos os valores da lista original maiores que o numero inteiro inserido."""
    filtrados = [x for x in lista if x > numero]
    list.sort(filtrados)
    return filtrados
    

def acima_da_media(notas):
    """Funcao que recebe as notas dos alunos de uma turma e retorna a meida da turma
    e uma lista ordenada com as notas que ficaram acima da media."""
    somaNotas = sum(notas)
    qtdNotas = len(notas)
    media = somaNotas/qtdNotas
    return m(notas,media)