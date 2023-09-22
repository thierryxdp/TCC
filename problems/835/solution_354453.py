def melhor_volta(matriz):
    '''funcao que retorna uma tupla que diz de quem foi a melhor volta prova informando o seu tempo e a volta que realiza esse tempo list(list) -> tupla''''
    
    menor_volta = float('inf')

    for corredor, voltas in enumerate(matriz):
       
    for numero_volta, tempo_volta in enumerate(voltas):

            if (tempo_volta < menor_volta):
                
                menor_volta = tempo_volta
                
                corredor_vencedor = (corredor + 1)
                
                volta_vencedora = (numero_volta + 1)


    return (corredor_vencedor, menor_volta, volta_vencedora)