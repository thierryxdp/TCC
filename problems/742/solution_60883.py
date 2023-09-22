def substitui(s,x,i):
    len(s)>i>=0
    return s.replace(str(s)[i-len(s)],str(x),1)
    if [i-len(s)] <0:
        return s.replace(str(s)[(i*1)-(len(s)-1)],str(x),1)