def inverte(frase):
    f1=str.replace(frase,","," ")
    
    f2=str.replace(f1,"."," ")
    
    f3=str.replace(f2,"-"," ")
    
    f4=str.replace(f3,"?"," ")
    
    f5=str.replace(f4,"!"," ")
    
    f5=f5.lower()

	f5=f5.split()
    
    f5=f5.reverse()

	list.join(f5)