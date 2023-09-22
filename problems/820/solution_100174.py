def posLetra (frase,letra,numero):
    ''' Entrada: Frase -> variável do tipo string
    			 Letra -> variável do tipo string
                 número -> indica a ocorrência desejada da letra(1 
                 para primeira ocorrência, 2 para a segunda,etc
                 variável do tipo inteiro
        
        Saída: A função retorna a posição(int) em que posição 
        	   da frase a ocorrência da letra está. Casp exista 
               menos ocorrências da letra do que a ocorrência pedida
               a função retorna -1
        
        str,str,int -> int'''
    i=0
    while i<len(frase):
        if letra in frase[numero]:
            return numero
        
        i=i+1