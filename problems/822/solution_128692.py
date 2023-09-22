def repetidos(num):
    '''funçao que ,dada uma lista de numeros,
  retorna o número de  vezes que um elemento 
  da lista é igual ao elemento anterior.  
  list->int'''
    i=1
    vezes=0
    while i<len(num):
        if num[i]==num[i-1]:
            vezes=vezes+1
        i=i+1
    return vezes