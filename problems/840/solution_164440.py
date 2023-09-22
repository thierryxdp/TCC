def bolos(A,B,C):
    """Essa função recebe parâmetros de quantidade de um produto para uma 
    receita (farinha,ovos,leite) e a partir da receita retorna se usando a
    quantidade especificada na receita quantos bolos irão conseguir fazer.
    Os argumentos são: A-Farinha de trigo;B-ovos;C-colher de leite. int,int"""
    far = A//2
    ovo = B//3
    leite = C//5
    if (A>2 or B>3 or C>5) and far ==ovo:
        return far
    elif (A>2 or B>3 or C>5) and far ==leite:
        return far
    elif (A>2 or B>3 or C>5) and ovo ==leite:
        return ovo
    elif (A>2 or B>3 or C>5) and far > leite:
        return leite
    elif (A>2 or B>3 or C>5) and far > ovo:
        return ovo
    elif A<2 or B<3 or C<5:
        return 0
    elif 4>A>=2 and B>3 and C>5:
        return 1
    elif A>2 and 6>B>=3 and C>5:
        return 1
    elif A>2 and B>3 and 10>C>=5:
        return 1
    else:
        return (A+B+C)//10