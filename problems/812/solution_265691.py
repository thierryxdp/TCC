def retira_pontuacao(x):
    A = x.replace(","," ")
    B = A.replace("."," ")
    C = B.replace("?"," ")
    return B