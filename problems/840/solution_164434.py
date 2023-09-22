def bolos(a,b,c):
    '''Retorna a quantidade de bolos que pode ser feita a partir da receita que requer 
    	2 xicaras de farinha de trigo, 3 ovos, e 5 colheres de sopa de leite a. Deve se
        informar a quantidade de xicaras de farinha de trigo (a), ovos (b) e colheres de 
        sopa de leite (c);
        float, int, float->int'''
    f=a//2
    o=b//3
    l=c//5
    return min(f,o,l)