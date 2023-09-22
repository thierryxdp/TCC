def insere(lista_numero,n):
    ''' Entrada: Lista_numero -> lista ordenada (crescente)
    			de números inteiros (dado do tipo list)
                 
                 n -> número que deve inserido na lista na posição
                correta (dado do tipo list)
                
        Saída: Lista ordenada e com o número adicionado
        
        list,int -> list'''
    
    lista_numero.append(n)
    list.sort(lista_numero)
    return lista_numero