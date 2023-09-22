def qtd_divisores(n):
    """Função que conta quantos divisores um número int tem; int -> int"""
    print([i for i in range(1, num//2+1) if num%i==0])