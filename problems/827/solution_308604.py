def qtd_divisores(n):
    d=0
    for i in range(n):
        if n%1==0 :
            a=1
        elif n%2==0 :
            b=1
        elif n%2==0 :
            c=1
        elif n%3==0 :
            d=1
        elif n%4==0 :
            e=1
        elif n%5==0 :
            f=1
        elif n%7==0 :
            g=1
        elif n%8==0 :
            h=1
        elif n%9==0 :
            i=1
        elif n%11==0 :
            j=1
        elif n%15==0 :
            k=1
        elif n%16==0 :
            l=1
        elif n%21==0 :
            m=1
        elif n%45==0 :
            o=1
        elif n%57==0 :
            p=1
        elif n%63==0 :
            a=1
        elif n%77==0 :
            q=1
        else :
            r=0
            d=a+b+c+d+e+f+g+h+i+j+k+l+m+o+p+q
    return d