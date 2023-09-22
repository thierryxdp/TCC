def uppCons(f):
    d = {"b":"B", "c":"C", "d":"D", "f":"F", "g":"G", "h":"H", "j":"J", "k":"K", "l":"L", "m":"M", "n":"N", "p":"P", "q":"Q", "r":"R", "s":"S", "t":"T", "v":"V", "w":"W", "x":"X", "y":"Y", "z":"Z"}
    for e in f:
        if e in d:
            str.replace(f,e,d[e]) 
return f