def colchao(a,b,c,h,l):
    ''''''
    if h>c and a<h:
        return True
    if h>b and c<l:
        return True
    else:
        return False