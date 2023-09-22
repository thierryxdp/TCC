def conta_numero(numero,matriz):
    '''Dado um numero inteiro e uma matriz de inteiros,
    a função conta e retorna quantas vezes esse numero
    aparece na matriz. int,list --> int'''
    
    soma=0
	
    for linha in matriz:
        if len(linha)==1:
            if linha==numero:
                soma=soma+1
                
        if len(linha)>1:
            for elemento in linha:
                if elemento==numero:
                    soma=soma+1
    return soma