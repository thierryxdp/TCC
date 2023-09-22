def faltante(lista):
     """funcao que dada uma lista com n inteiros de 1 a n, descobre qual numero
     está faltando na lista. list->int"""
     i=1
     n= [1,2,3,4,5,6,7,8,9,10]
     while i<len(lista):
         if n[i] in lista[i]:
            i=i+1
     return i+1