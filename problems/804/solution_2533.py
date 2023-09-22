def filtra_pares(k):
        if k[0]%2==0 and k[1]%2==0 and k[2]%2==0 and k[3]%2==0:
                return (k[0],k[1],k[2],k[3])
        if k[0]%2!=0 and k[1]%2==0 and k[2]%2==0 and k[3]%2==0:
                return (k[1],k[2],k[3])
        if k[0]%2==0 and k[1]%2!=0 and k[2]%2==0 and k[3]%2==0:
                return (k[0],k[2],k[3])
        if k[0]%2==0 and k[1]%2==0 and k[2]%2!=0 and k[3]%2==0:
                return (k[0],k[1],k[3])
        if k[0]%2==0 and k[1]%2==0 and k[2]%2==0 and k[3]%2!=0:
                return(k[0],k[1],k[2])
        if k[0]%2!=0 and k[1]%2!=0 and k[2]%2==0 and k[3]%2==0:
                return(k[2],k[3])
        if k[0]%2!=0 and k[1]%2==0 and k[2]%2!=0 and k[3]%2==0:
                return(k[1],k[3])
        if k[0]%2!=0 and k[1]%2==0 and k[2]%2==0 and k[3]%2!=0:
                return(k[1],k[2])
        if k[0]%2==0 and k[1]%2!=0 and k[2]%2!=0 and k[3]%2==0:
                return(k[0],k[3])
        if k[0]%2==0 and k[1]%2!=0 and k[2]%2==0 and k[3]%2!=0:
                return(k[0],k[2])
        if k[0]%2==0 and k[1]%2==0 and k[2]%2!=0 and k[3]%2!=0:
                return(k[0],k[1])
        if k[0]%2!=0 and k[1]%2!=0 and k[2]%2!=0 and k[3]%2==0:
                return(k[3], )
        if k[0]%2==0 and k[1]%2!=0 and k[2]%2!=0 and k[3]%2!=0:
                return(k[0])
        if k[0]%2!=0 and k[1]%2==0 and k[2]%2!=0 and k[3]%2!=0:
                return(k[1])
        if k[0]%2!=0 and k[1]%2!=0 and k[2]%2==0 and k[3]%2!=0:
                return(k[2])
        if k[0]%2!=0 and k[1]%2!=0 and k[2]%2!=0 and k[3]%2!=0:
                return ()