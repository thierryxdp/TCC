def bolos(a,b,c):
    if (a>=2)and(b>=3)and(c>=5)and(a%2==0)and(b%3==0)and(c%5==0)and((a+b+c)%10==0):
        return (a+b+c)/10
    if (a<2)or(b<3)or(c<5):
        return 0
    else:
        return ceil(((a+b+c)/10)-1)