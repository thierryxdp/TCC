def filtra_pares(s):
    """Função que recebe uma tupla com quatro elementos inteiros como 
    parâmetro, e retorna uma nova tupla contendo apenas os elementos 
    pares da tupla original na mesma ordem. Assinatura: tuple->tuple"""
    if s[0]%2==0:
        n=s[0]
    if s[1]%2==0:
        n=s[1]
    if s[2]%2==0:
        n=s[2] 
    if s[3]%2==0:
        n=s[2]
        return n
    else:
        return ()