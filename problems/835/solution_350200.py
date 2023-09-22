def melhor_volta(matriz):
    """Função que, dada uma matriz 6x10 com os tempos em segundos de corredores em cada uma de suas voltas, retorna uma tupla informando de quem foi a melhor volta da prova, com qual tempo e em que volta; lista->tupla"""
    
    menorTempo = min(min(matriz[0]),min(matriz[1]),min(matriz[2]),min(matriz[3]),min(matriz[4]),min(matriz[5]))
    
    for lista in matriz:
        
        for n in lista:
            
            if n == menorTempo:
                
                corredor = list.index(matriz,lista) + 1
                
                volta = list.index(lista,n) + 1
                
    return (corredor,menorTempo,volta)