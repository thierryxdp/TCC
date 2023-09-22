def melhor_volta(matriz):
    l=0
    c=0
    tempo=99999999999999999999999999999999
    volta=0
    piloto=0
    while l < len(matriz):
        while c <len (matriz[0]):
            if matriz[l][c] < tempo :
                tempo = matriz[l][c]
                volta= c+1
                piloto=l+1
            c+=1     
        l+=1
        
    return piloto,tempo,volta