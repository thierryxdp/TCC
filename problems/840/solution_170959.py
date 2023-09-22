def bolos(A,B,C):
    '''função que tem como entrada a quantidade de ingredientes para fazer bolo, sendo
    	A xicaras de farinha, B ovos e C colheres de sopa de leite e retorna quantos
        bolos serão possiveis fazer'''
    if A%2=0 and B%3=0 and C%5=0:
        if A/2 == B/3 == C/5:
            return (A+B+C)/10
        elif A/2 =! B/3 and A/2 =! C/5 and B/3 == C/5:
            return A/2
        elif A/2 =! B/3 and B/3 =! C/5 and A/2 == C/5:
            return B/3
        elif A/2 =! C/5 and B/3 =! C/5 and A/2 == B/3:
            return C/5