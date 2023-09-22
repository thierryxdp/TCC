def colchao(medidas,H,L):
    """Função que recebe a altura H e largua L de uma porta,
    além das medidas A,B e C de um colchão e retorna True se
    o colchão for capaz de passar pela porta. Caso contrário,
    a função retornará False.
    Entrada: Lista(int,int,int), int, int
    Saída: Bool
    """
    A = medidas[0]
    B = medidas[1]
    C = medidas[2]
    medidas = [A,B,C]
    
    
    if C<L or B<H or (B<L) or  (A<L):
        return True
    
    else:
        return False