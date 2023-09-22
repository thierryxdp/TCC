def dimensao(d,h,l):
    if(((d[0]<=h)and (d[1]<=1) or(d[1]<=h)) and (d[0]<=1) or ((d[0]<=h) and (d[2]<=1) or (d[2]<=h)and(d[0]<=1)) or ((d[1]<=h)and(d[2]<=1)or(d[2]<=h)and(d[1]<=1))):
        return True
    else:
        return False