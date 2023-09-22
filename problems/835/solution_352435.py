def melhor_volta(matriz):
    volta=-1
    corredor=-1
    tempo=[]
    for i in matriz:
        corredor+=1
        tempo+=[min(i)]
        volta=0
        for j in i:
            volta+=1
    tempo=min(tempo)        
    return (corredor,tempo,volta)        
            
melhor_volta([[41,55, 77, 56, 97, 68, 17, 14, 8, 19], [20, 22, 29, 61, 33, 30, 6, 83, 65, 66], [28, 86, 78, 16, 7, 99, 47, 34, 42, 46], [92, 12, 15, 57, 54, 21, 18, 23, 76, 45], [80, 24, 43, 25, 3, 58, 93, 62, 26, 67], [40, 35, 48, 94, 13, 9, 82, 73, 87, 49]])