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

def acima_da_media (lista_notas):
    ''' Entrada: Lista_notas -> parametro do tipo
    			list
         
         Saída: lista ordenada com as notas que
         ficaram acima da média das notas
         
         list -> list'''
    
    media = (sum(lista_notas))/(len(lista_notas))
    return maiores (lista_notas,media)