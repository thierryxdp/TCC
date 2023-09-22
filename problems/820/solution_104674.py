def posLetra(frase,L,n):
    '''Função que recebe uma str, uma letra e a ocorrência da letra e retorna em que posição da str aquela ocorrência da letra estará
    str, str, int -> int'''

    teste = 0
    contador = 0 

    while teste < len(frase):
        #enquanto  o contador for menor que o tamanho da str
        
        if L in frase:
            #se a letra estiver dentro da frase
            if frase[teste] == L:
                #e se o elemento da frase for igual a letra
                contador += 1
                    #adicionará +1 ao contador
            elif contador == n:
                    #quando o contador for igual a ocorrência desejada  
                ocorrencia_letra = int(teste-1)
                    #nos informará a posição que elá estará
                return ocorrencia_letra  
        teste += 1
                    
    return -1