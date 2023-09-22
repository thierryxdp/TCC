def posLetra(p,l,n):
    i=0
    while i<len(p):
        if l in p:
            if str.count(p,l)==1:
                if n==1:
                    posicao=str.find(p,l)
                if n==2:
                    posicao=str.find(p,l,(str.find(p,l)+1))
   
            if str.count(p,l)>1:
                if n==1:
                    posicao=str.find(p,l)
                if n==2:
                    posicao=str.find(p,l,(str.find(p,l)+1))
                if n==3:  
                    posicao=str.find(p,l,str.find(p,l,(str.find(p,l)+1))+1)
                if n==4:
                    posicao=str.find(p,l,str.find(p,l,str.find(p,l,(str.find(p,l)+1))+1)+1)
                if n==5:
                    posicao=str.find(p,l,str.find(p,l,str.find(p,l,str.find(p,l,(str.find(p,l)+1))+1)+1)+1)
                    
                    
        return posicao