def filtra_pares(n1,n2,n3,n4):
    """dados quatro numeros inteiros em sequencia retorna-se os pares dos mesmos na respectiva ordem
    n1->numero 1
    n2->numero 2
    n3->numero 3
    n4->numero 4
    int,int,int,int->int"""
    lista1=[n1,n2,n3,n4]
	lista2=[]
	for valor in lista1:
    	if valor%2==0:
        	lista2.append(valor)