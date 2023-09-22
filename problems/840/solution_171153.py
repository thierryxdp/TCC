def bolos(A,B,C):
    """Essa função calcula quantos bolos se consegue fazer com os ingredientes possuidos
    A para quantidade de xícaras de trigo
    B para quantidade de ovos
    C para quantidade de colheres de sopa de leite
    Retorna a quantidade bolos que possam ser feitos."""
    return min(A//2,B//3,C//5)
#Essa função sabendo que o ingredientes mínimos para fazer o bolo são A=2, B=3 e C=5.Ela calcula a divisão entre os valores dados e os necessários para o bolo  e com módulo math.floor o arredonda para o menor inteiro.
#int,int,int → int