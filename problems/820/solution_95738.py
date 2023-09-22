def posLetra(string,letra,pos):
    qnts=string.count(letra)
    while pos<=qnts or pos>qnts:
        if pos==1:
            resp=string.find(letra)
            return resp
        elif pos==qnts:
            if pos==3:
                resp=string.find(letra,qnts+6)
                return resp
            else:
                resp=string.find(letra,qnts)
                return resp
        elif pos>1 and pos<=qnts:
            if string.find(letra)==string.find(letra,pos):
                resp=string.find(letra,string.find(letra)+1)
                return resp
            else:
                resp=string.find(letra,qnts+pos+9)
                return resp
        elif pos>qnts:
            resp=-1
            return resp