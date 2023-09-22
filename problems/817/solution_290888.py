#3
def insere(lista_numero,n):
    """dada de entrada uma lista(lista_numero) de números int na ordem crescente, retorna uma lista também ordenada acom a adição de n
    list,int==>list"""
    list.append(lista_numero,n)
    list.sort(lista_numero)
    return lista_numero
#4
def maiores(lista_int,n):
    """Dada uma lista(lista_int), retorna todos números da lista maiores que n
list,int==>list"""
    nova_lista = insere(lista_int,n)
    return nova_lista[list.index(nova_lista,n)+1:]
#5
def acima_da_media(lista_notas):
    """Dada uma lista com as notas de uma turma, retorna todos os valores acima da média da turma
    list=>list"""
    média=sum(lista_notas)/len(lista_notas)
       return maiores(lista_notas, média)