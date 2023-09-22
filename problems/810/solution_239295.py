def inverte(f):
    
    f1= str.replace((str.lower(f)),"-"," ")
    f2= str.replace(f1,","," ")
    f3= str.replace(f2,":"," ")
    f4= str.replace(f3,";"," ")
    f5= str.replace(f4,"?"," ")
    f6= str.replace(f5,"!"," ")
    f7= str.replace(f6,"."," ")
    L1= str.split(f7)
    s=str.join(" ",L1[0:-1])
    return s