def qtd_divisores(n):
    d=0
    for i in range(n):
        if  n%1==0 and  n%3==0 and  n%19==0 and n%57==0 :
            d=4
        elif n%1==0 and  n%2==0 and  n%4==0 and n%8==0 and n%16==0:
            d=5
        elif n%1==0 and n%3==0 and  n%5==0 and  n%9==0 and n%15==0  and n%45==0:
            d=6
        elif n%1==0 and  n%3==0 and  n%7==0 and n%9==0 and n%21==0 and  n%63==0:
            d=6
        elif n%1==0 and  n%7==0 and  n%11==0 and n%77==0 :
            d=4
        elif n%1==0 and  n%2==0 and  n%13==0 and n%26==0:
            d=4
        else:
            d=0
    return d