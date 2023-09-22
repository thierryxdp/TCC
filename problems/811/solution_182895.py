# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis

def colchao(medidas,H,L):
    [A,B,C]=medidas
    
    if (A<L and B<H) or (A<L and C<H) or (B<L and A<H) or (B<L and C<H) or (C<L and A<H) or (C<L and B<H):
        return True
    else:
        return False