def colchao(medidas,H,L):
    """Função que recebe a altura H e largua L de uma porta,
    além das medidas A,B e C de um colchão e retorna True se
    o colchão for capaz de passar pela porta. Caso contrário,
    a função retornará False.
    Entrada: Lista(int,int,int), int, int
    Saída: Bool
    """
    
    medidas = [A,B,C]
    
    if (C<L and B<H) or (B<L and C<H) or  (A<L and C<H):
        return True
    
    else:
        return False