def bolos (A,B,C):
    '''Calcula a quantos bolos João consegue fazer, dado os parâmetros A,B,C. 
    int,int,int-->int'''
    if A//2>=1:
        if B//3>=1:
            if C//5>=1:
                return min((A//2),(B//3),(C//5))
    if A//2<=0:
        return (0)
    if B//3<=(0):
        return (0)
    if C//5<=0:
        return (0)