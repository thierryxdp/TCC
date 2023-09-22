def eh_quadrada(s):
    d=len(s)
    if(len(s)!=0 and len(s)==len(s[d-1])):
        return True
    elif(len(s)==0):
        return True
    else:
        return False