#Start your python function here
def filtra_pares(t:tuple)->tuple:
    """ recebe uma tupla de 4 números inteiros e retorna uma nova tupla contendo apenas pares"""
    t1 = t[0]
    t2 = t[1]
    t3 = t[2]
    t4 = t[3]
    if t1 % 2 == 0 and t2 % 2 == 0 and t3 % 2 == 0 and t4 % 2 == 0:
      return (t1,t2,t3,t4)
    elif t1 % 2 == 0 and t2 % 2 == 0 and t3 % 2 == 0:
      return (t1,t2,t3,)
    elif t1 % 2 == 0 and t2 % 2 == 0 and t4 % 2 == 0:
      return (t1,t2,t4,)
    elif t1 % 2 == 0 and t3 % 2 == 0 and t4 % 2 == 0:
      return (t1,t3,t4,)
    elif t2 % 2 == 0 and t3 % 2 == 0 and t4 % 2 == 0:
      return (t2,t3,t4,)
    elif t1 % 2 == 0 and t2 % 2 == 0:
      return (t1,t2,)
    elif t1 % 2 == 0 and t3 % 2 == 0:
      return (t1,t3,)
    elif t1 % 2 == 0 and t4 % 2 == 0:
      return (t1,t4,)
    elif t2 % 2 == 0 and t3 % 2 == 0:
      return (t2,t3,)
    elif t2 % 2 == 0 and t4 % 2 == 0:
      return (t2,t4,)
    elif t3 % 2 == 0 and t4 % 2 == 0:
      return (t3,t4,)
    elif t1 % 2 == 0:
      return (t1,)
    elif t2 % 2 == 0:
      return (t2,)
    elif t3 % 2 == 0:
      return (t3,)
    elif t4 % 2 == 0:
      return (t4,)
    else:
        return ()