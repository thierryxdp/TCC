def repetidos (listaN):
    i=0
    resultado=[]
    while i < len(listaN):
        if listaN[i-1]==listaN[i]:
            resultado=resultado+[listaN[i],]
        i=i+1    
    return len(resultado)
'''funcao que recebe uma lista de numeros e 
retorna o numero de vezes que um elemento igual
ao elemento no indice anterior
list->int'''