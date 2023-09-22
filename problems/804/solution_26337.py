def filtra_pares (pares):
    """Função que dados uma tupla com quatro elementos inteiros
    como entrada, retorna uma nova tupla contendo apenas os elementos
    pares da tupla original, na mesma ordem em que se encontravam;
    tupla -> tupla"""
   
    par1= A[0]
    par2= A[1]
    par3= A[2]
    par4= A[3]


    parA = int(par1)%2
    parB = int(par2)%2
    parC = int(par3)%2
    parD=  int(par4)%2

    P1= par1,par2,par3,par4
    P2= par1,par2,par3
    p3= par1,par2,par4
    p4= par1,par3,par4
    p5= par1,par2
    p6= par1,par3
    p7= par1,par4
    p8= par2,par3,par4
    p9= par2,par3
    p10= par2,par4
    p11= par3,par4
    vazio = ()

   
    if parA==0 and parB==0 and parC==0 and parD==0:
      return P1
    else:
       if parA==0 and parB==0 and parC==0 and parD!=0:
           return p2
       elif parA==0 and parB==0 and parC !=0 and parD==0:
           return p3
       else:
            if parA==0 and parB!=0 and parC==0 and parD==0:
               return p4
            elif parA== 0 and parB==0 and parC!=0 and parD!=0:
               return p5
            else:
                if parA==0 and parB!=0 and parC==0 and parD!=0:
                    return p6
                elif parA==0 and parB!=0 and parC!=0 and parD==0:
                    return p7
                else:
                    if parA!=0 and parB==0 and parC==0 and parD==0:
                        return p8
                    elif parA!=0 and parB==0 and parC==0 and parD!=0:
                        return p9
                    else:
                        if parA!=0 and parB==0 and parC!=0 and parD==0:
                            return p10
                        elif parA!=0 and parB!=0 and parC==0 and parD==0:
                            return p11
                        else:
                            if parA==0 and parB!=0 and parC!=0 and parD!=0:
                              return (a,)
                            elif parA!=0 and parB==0 and parC!=0 and parD!=0:
                              return (b,)
                            else:
                                if parA!=0 and parB!=0 and parC==0 and parD!=0:
                                    return (c,)
                                elif parA!=0 and parB!=0 and parC!=0 and parD==0:
                                    return (d,)
                                else:
                                    return ()