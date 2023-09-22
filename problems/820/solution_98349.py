def posLetra(tex, let, num):
    i = 0
    rep = 0
    posi = 0
    if(tex.count(tex) > num):
        while(i<len(tex) and rep<num):
            if(tex[i] == let):
                rep += 1
                i += 1
            else:
                i += 1     
        return i - 1  
    else:
        return -1