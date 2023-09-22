def colchao(medidas, H, L):
    '''
    tendo sido informada a lista possuindo as medidas
    do colchão, a altura H das portas e a largura L das
    mesmas, retorna True caso o colchão possa passar
    das portas e False caso não possa
    
    list, int, int -> bool
    
    as medidas devem ser informadas na forma
    [A, B, C], onde A, B e C são parâmetros do tipo int
    '''
    dim_porta = [H, L]
    dim_porta.sort(reverse = True)
    medidas.sort(reverse = True)
    return medidas[1]<=dim_porta[0] and medidas[2]<=dim_porta[1]