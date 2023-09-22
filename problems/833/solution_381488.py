def conta_numero(numero,matriz):
    '''Função que dado um número e a matriz qualquer,
conta e retorna quantas vezes o número aparece na matriz.
    int, list -> int'''
    
    contagem = []
    
    for lista in matriz:
        for elemento in lista:
            i=0
            if elemento[i] == numero:
            	contagem.append(i)
           		i+=1
    return len(contagem)