def maiores (lista_numeros_inteiros,n):
    ''' Entrada: lista_numero_inteiros -> parametro
    			do tipo list 
                 n -> parametro do tipo int
        
         Saída: Lista contendo os números maiores que
        	   o parametro n dado
               
               list,int -> list'''
    
    if n not in lista_numeros_inteiros:
        lista_numeros_inteiros.append(n)
        list.sort(lista_numeros_inteiros)
        centro = lista_numeros_inteiros.index(n)
        lista2 = lista_numeros_inteiros[centro+1:]
        return lista2
    if n in lista_numeros_inteiros:
        list.sort(lista_numeros_inteiros)
        centro = lista_numeros_inteiros.index(n)
        lista3 = lista_numeros_inteiros[centro+1:]
        return lista3