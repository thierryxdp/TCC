def bolos(A,B,C):
    '''
    Entrada:
        Os parâmetros de entrada da função são três números inteiros A,B e C que coorespondem a:  
        A = xícara
        B = ovos               ----> int
        C = colheres
    Saída:
        Calcula a quantidade máxima de bolos ----> int
    '''
    return round(((A/2 + B/3 + C/5)/3) - 0.5)