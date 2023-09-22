def melhor_volta(m):
        c=0
        p=0
        g=()
        d=()
        for i in range(0,6):
                for n in range(0,10):
                        d=d+(m[i][n],)
        for i in range(0,6):
                for n in range(0,10):
                        if min(d)==m[i][n]:
                                c=i
                                p=n
                                break
        return (c,min(d),i)