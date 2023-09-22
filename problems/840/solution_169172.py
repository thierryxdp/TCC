def bolos(a,b,c):
    ''' 
    	A função defini a quantidade máxima de bolos que
    	pedrinho pode fazer, considerando que cada bolo 
        leva os ingredientes na quantidade exata da receita.
        Sendo A o número de xicaras de farinha,
        B o número ovos e C o número de colheres de sopa 
        de leite.
    '''
    return min((a//2),(b//3),(c//5))