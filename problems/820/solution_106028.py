def posLetra(texto,letra,numero):
    '''str,str,int -> int'''
    '''retorna o index da enesima ocorrencia da letra no texto, -1 caso nn apareça'''
    
    c = str.count(texto,letra)
    i = 0
    
    if c - numero < 1:
        return -1
    
    else:
        while c - numero + 1 < str.count(texto,letra,i):
            i += 1
            pass
        else:
            return str.index(texto,letra,i)