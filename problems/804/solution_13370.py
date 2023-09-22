def filtragem (x):
    final = ()
    if  x[0]%2 == 0:
         final +=  (x[0],) 
    if x[1]%2==0:
         final += (x[1],)
    if x[2]%2==0:
         final += (x[2],)
    if x[3]%2==0:
         final =+ (x[3],)
    return final