def intercala(lista1, lista2):
    """Função para intercalar lista 1 e lista 2 criando uma nova lista
    com 3 elementos"""
lista1=[1,3,5]
lista2=[2,4,6]
int("original lista1:"+(lista1))
int("original lista2:"+(lista2))
res= lista1+lista2
res[::2}=lista1
res[1::2]=lista2
int (a intercalacao da lista e:"str(res))