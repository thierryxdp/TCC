def bolos(A,B,C):
    """Essa função recebe parâmetros de quantidade de um produto para uma 
    receita (farinha,ovos,leite) e a partir da receita retorna se usando a
    quantidade especificada na receita quantos bolos irão conseguir fazer.
    Os argumentos são: A-Farinha de trigo;B-ovos;C-colher de leite. int,int"""
    if A<2 and B<3 and C<5:
        return "Sem bolo"
    elif A>=2 and B>=3 and C>=5:
        return (A+B+C)//10