def bolos (A,B,C,a,b,c):
    '''Funcao que calcula o numero de bolos feitos seguindo a receita com A xic  de farinha, B ovos e C colheres de sopa de leite'''
    if A<2:
        return 0
    if B<3:
        return 0
    if C<5:
        return 0
    else a=A//2 and b=B//3 and c=C//5:
	return min(a,b,c)