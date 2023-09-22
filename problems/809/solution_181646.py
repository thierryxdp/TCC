def intercala(list1, list2):
    """Função para intercalar lista 1 e lista 2 criando uma nova lista
    com 3 elementos"""
list1=[1,3,5]
list2=[2,4,6]
int("original list1:"+(list1))
int("original list2:"+(list2))
res= list1+list2
res[::2}=list1
res[1::2]=list2
int (a intercalacao da list e:"str(res))