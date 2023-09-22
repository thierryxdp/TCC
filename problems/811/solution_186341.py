colchao(medidas, H, L):
    '''
    tendo sido informada a lista possuindo as medidas
    do colchão, a altura H das portas e a largura L das
    mesmas, retorna True caso o colchão possa passar
    das portas e False caso não possa
    
    list, int, int -> bool
    
    as medidas devem ser informadas na forma
    [A, B, C], onde A, B e C são parâmetros do tipo int
    '''
    medidas_ordenadas = medidas.sort(reverse = True)
    tamanho_porta = [H, L].sort(reverse = True)
    return [H, L][0] < medidas_ordenadas[0] and [H, L][1] < medidas_ordenadas[1]