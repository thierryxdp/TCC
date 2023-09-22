def melhor_volta(m):
        c=0
        p=0
        g=()
        d=()
        for i in range(len(m)):
                for n in range(len(m[0])):
                        d=d+(m[i][n],)
        for i in range(len(m)):
                for n in range(len(m[0])):
                    
                        if min(d)==m[i][n]:
                                c=i+1
                    			p=n
               			break
        return (c,min(d),i)