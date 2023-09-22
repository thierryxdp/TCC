def colchao(medias,H,L):
    A= medidas[0]
    B= medidas[1]
    C= medidas[2]
    if(A<H or A==H) and (B<L or B==L):
        return True
    elif(A<L or A==L) and (B<H or B==H):
        return True
    elif(B<L or B==L) and (C<H or C==H):
        return True
    elif(C<L or C==L) and (B<H or B==H):
        return True
    elif(A<H or A==H) and (C<L or C==L):
        return True
    elif(A<L or A==L) and (C<H or C==H):
        return True
    else: 
        return False