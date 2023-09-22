def colchao(d,h,l):
    if(((d[0]<=h)and(d[1]<=l)or(d[1]<=h))and(d[0]<=l)or((d[0]<=h)and(d[2]<=l)or(d[2]<=h)and(d[0]<=l))or((d[1]<=h)and(d[2]<=l)or(d[2]<=h)and(d[1]<=l))):
        return True
    else:
        return False