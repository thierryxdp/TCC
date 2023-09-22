def maiores(lista,num):
    """Função que, dada uma lista de números inteiros e um número 'n', retorna
outra lista que contenha apenas os números da lista maiores que 'n'."""
    """list-->list"""
    resultado=[]
    for c in lista:
        if c > num:
            resultado.append(c)
    list.sort(resultado)
    return resultado
        
def acima_da_media(notas):
    """Função que recebe as notas dos alunos de uma turma e retorna uma lista
ordenada com as notas que ficaram acima da média."""
    """list-->list"""
    media=sum(notas)/len(notas)
    return maiores([notas,media])