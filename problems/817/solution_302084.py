def maiores(conjunto,n):
    
    if n in conjunto:
        list.sort(conjunto)
        junto1= conjunto[list.index(conjunto,n)+1:]
      
        return junto1
    
    
    else:
        conjunto.insert(-1,n)
        list.sort(conjunto)
        junto1= conjunto[list.index(conjunto,n)+1:]
      
        return junto1

def acima_da_media(base):
    
    m= int(sum(base)//len(base))
    
    return maiores(base,m)