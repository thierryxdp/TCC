#3
def bolos(A,B,C)->int:
    '''o // vai garantir q seja o maior número inteiro e o min encontrará o limitante e quantos bolos são possíveis fazer com o limitante''' 
    return min((A//2),(B//3),(C//5))