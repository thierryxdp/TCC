def maiores(listadenumerosinteiros,n):
    """Funcao  que recebe uma lista de numeros inteiros e um numero inteiro n, retorna uma lista com os numeros maiores que n e em ordem cresecente. list,int=>list"""
    list.insert(listadenumerosinteiros,0,n)
    list.sort(listadenumerosinteiros)
    return listadenumerosinteiros[list.index(listadenumerosinteiros,n)+list.count(listadenumerosinteiros,n):]

def acima_da_media(notas):
    """Funcao que recebe uma lista com as notas de de alunos de uma turma e retorna uma lista com as notas que ficaram acima da media. list=>list"""
    media= sum(notas)/len(notas)
    return maiores(notas,media)