def repetidos(lista):
'''dada uma lista de numeros e retorne o numero de vezes que o elemento da lista igual ao elemento anterior
:param lista: list->list
:return; int->int
'''
i=0
contador= 0
repete= 0
while contador < len(lista):
    if lista[i] ==lista[i-1]:
        repete+=1
        
              i+=1
              contador+=1
         
    return repete