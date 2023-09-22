# Questão 3

def posLetra(frase,L,n):
    '''Função que recebe uma str, uma letra e a ocorrencia da letra e retorna
    em que posição da str aquela ocorrência da letra estará'''

    teste = 0
    contador = 0 

    while teste < len(frase):
        #enquanto  o contador for menor que o tamanho da str
        
        if L in frase:
            #se a letra estiver dentro da frase nos dada

            if frase[teste] == L:
                #e se a o elemento da frase for igual a letra

                contador = contador + 1
                    # se for igual adicionará +1 ao contador

            elif contador == n:
                    # quando o contador for igual a ocorrência desejada
                    
                ocorrencia_letra = int(teste-1)
                    # nos informará a posição que elá estará

                return ocorrencia_letra
                    
            elif frase[teste] == len(frase) and contador != n:
                # porém se chegar no  final da frase e o contador for menor do que a ocorrencia indicada 
                
                return -1

        teste = teste +1