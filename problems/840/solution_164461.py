def bolos (A,B,C):
    """Dadas as quantidades de xícaras de farinha(A), ovos(B) e colheres de leite(C); calcula a quantidade possivel de bolos que podem ser feitos seguindo a receita;
    	int, int, int -> int"""
    return ((A//2)+(B//3)+(C//5))//3