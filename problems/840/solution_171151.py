def bolos(a,b,c):
    '''funçao que calcula a quantidade máxima de bolos que é possível fazer com 'a' xícaras de farinha, 'b' ovos e 'c' colheres de leite, sendo que para fazer um único
bolo serão necessarios 2 xícaras de farinha,3 ovos e 5 colheres  sopa de leite;
    int,int,int->int'''
    return int(min(a//2,b//3,c//5))