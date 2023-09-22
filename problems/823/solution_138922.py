def faltante(lista):
	''' Dada uma funçao que verifica qual número do 
    intervalo de uma lista está faltando; list->int'''
    i=0
	s= []
    list.sort(lista)
    while i<len(lista)+1:
        s= s+[i+1,]
        i= i+1
        a= sum(s)
        b= sum(lista)
        return a-b