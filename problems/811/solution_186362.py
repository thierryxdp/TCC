def colchao(s,d,h):
    if(s[0]<d and s[1]<h):
        return True
    elif(s[0]<h and s[1]<d):
        return True
    else:
        return False