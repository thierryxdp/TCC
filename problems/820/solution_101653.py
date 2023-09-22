def posLetra (frase,letra,ocorrencia):
    ''' Entrada: Frase -> variável do tipo string
    			 Letra -> variável do tipo string
                 ocorrencia -> indica a ocorrência desejada da letra(1 
                 para primeira ocorrência, 2 para a segunda,etc
                 variável do tipo inteiro
        
        Saída: A função retorna a posição(int) em que posição 
        	   da frase a ocorrência da letra está. Caso exista 
               menos ocorrências da letra do que a ocorrência pedida
               a função retorna -1
        
        str,str,int -> int'''
    i = 0
    lista=[]
    if ocorrencia <= frase.count(letra):
        while i < len(frase):
            if frase[i] in letra:
                lista.append(i)
            i+=1
        return lista[ocorrencia-1]
    else:
        return -1