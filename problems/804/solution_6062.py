def filtra_pares(x):
    num_1 = x[0]
    num_2 = x[1]
    num_3 = x[2]
    num_4 = x[3]
    tuplaB = ()
    if num_1%2 == 0:
        tuplaB = tuplaB+(num_1,)
    if num_2%2==0:
        tuplaB = tuplaB+(num_2,)
    if num_3%2 ==0:
        tuplaB= tuplaB+(num_3,)
    if num_4%2 ==0:
        tuplaB = tuplaB+(num_4,)
    return tuplaB