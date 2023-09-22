def jogo(a,b):
    if a>b:
        return 3
    if a==b:
        return 1
    else:
        return 
def pontos_por_time(L):

    p1=int
    p2=int

    if L[0][0]==L[1][0]:
        p1==jogo(L[0][2][0],L[0][2][1])+jogo(L[1][2][0],L[1][2][1])
    	p2==jogo(L[0][2][1],L[0][2][0])+jogo(L[1][2][1],L[1][2][0])
    if L[0][1]==L[1][0]:
        p1==jogo(L[0][2][0],L[0][2][1])+jogo(L[1][2][0],L[1][2][1])
    	p2==jogo(L[0][2][1],L[0][2][0])+jogo(L[1][2][1],L[1][2][0])
    return dict(L[0][0]=p1,L[0][1]=p2)