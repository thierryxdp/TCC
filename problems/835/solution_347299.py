def melhor_volta(temposCorredores):

    melhorCorredor = 1,temposCorredores[0][0]

    for i in range(len(temposCorredores)):
        if min(temposCorredores[i]) < melhorCorredor[1]:
            melhorCorredor = i + 1, min(temposCorredores[i])

    return melhorCorredor