def conta_numero(numero,matriz):
    '''Conta e retorna o número de vezes que um número
       aparece em uma matriz, ambas passadas como valor
       de entrada;
       int, list -> int'''
    
    contagem = 0
    
    for linha in matriz:
        
        for coluna in linha:
            
            if coluna == numero:
                
                contagem += 1
                
    return contagem