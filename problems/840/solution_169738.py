def numero_bolos(a,b,c):
    """Função que calcula a quantidade máxima de bolos que se pode fazer com uma determinada quantidade de ingredientes, sabendo que para 1 bolo são necessários 2 xícaras de farinhad e trigo, 3 ovos e 5 colheres de sopa de leite, dados a quantidade de ingredientes que se possui atualmente. int,int,int -> int"""
    return min(a//2,b//3,c//5)