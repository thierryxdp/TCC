# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
def intercala(lista1, lista2):
    """ Função que recebe duas listas com 3 elementos e retorna uma nova lista com os valores da lista 1 e da lista 2 intercalados
        (1) A vaiável lista_final é o resultado da lista1 intercalada com a lista 2.
        (2) A varável cont vai ser utilizada como um marcador de indice para a lista 2.
        (3) Caso uma das listas tenha um tamanho menor ou maior do que 3 elementos, o programa vai exibir uma mensagem falando que uma das listas
        não tem o tamanho correto.

        caso seja iserido valores validos        ==>   list,list --> list
        caso algum valor invalido seja inserido  ==>   list, list --> str"""
    intercala = []
    cont = 0

    for j in [lista1,lista2]:
        if len(j) > 3:
            return "Uma ou mais lista tem tamanho maior do que 3 elementos!"
        elif len(j) < 3:
            return "Uma ou mais lista tem tamanho menor do que 3 elementos!"

    for i in lista1:
        intercala.append(i)
        intercala.append(lista2[cont])
        cont += 1

    return intercala