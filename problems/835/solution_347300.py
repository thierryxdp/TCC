def melhor_volta(temposCorredores):

    melhorCorredor = 1,10000,1

    for i in range(len(temposCorredores)):
        for j in range(len(temposCorredores[0])):
            if temposCorredores[i][j] < melhorCorredor[1]:
                melhorCorredor = i+1, temposCorredores[i],j+1
            

    return melhorCorredor