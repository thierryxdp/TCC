def conta_numero(numero,matriz):
    """Função que, dado um número inteiro e uma matriz de inteiros de tamanho qualquer, conta e retorna quantas vezes aquele número aparece na matriz; int,lista->int"""
    
    contagem = 0
    
    for listas in matriz:
        
        for n in listas:
            
            if n == numero:
                
                contagem = contagem + 1
                
    return contagem