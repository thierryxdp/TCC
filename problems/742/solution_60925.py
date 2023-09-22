def substitui(s,x,i):
    len(s)>i>=0
    return s.replace(str(s)[i-len(s)+(len(s)+1)],str(x),1)