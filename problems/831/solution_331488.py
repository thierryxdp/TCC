def lingua_p(s):
    i=0
    ss=s.lower()
    myc=list(ss)
    while i < len(s):
        if ss[i] in 'AEIOUaeiouãéêàáíú':
            del myc[i]
            myc.insert(i,ss[i] + 'p' + ss[i])
        i+=1
    return ''.join(myc)