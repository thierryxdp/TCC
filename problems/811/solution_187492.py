def colchao(A,B,C,H,L):
    '''Dados as medidas em centimetro-->int, retorna (True), caso o colchao passe pela porta e (False), caso nao passe '''
    if(A>B):
        TR==A
        A==B
        B==TR
    elif(B>C):
        TR=C
        B==C
        C==TR
    elif(A>B):
        TR==A
        A==B
        B==TR
    elif(L>H):
        TR==H
        H==L
        L==TR
    if (L>=A and H>=B):
        return True
    else:
        return False