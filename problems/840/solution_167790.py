def bolos(a,b,c):
    """Calcula quantas receitas de bolo sao possiveis de ser
    realizadas dadas as quantidades mínimas necessárias de cada
    igrediente"""
     return min((a//2)+(b//3)+(c//5))