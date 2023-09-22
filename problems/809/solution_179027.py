def intercala(L1, L2):
    if L1 and L2:
        return 'intercala'(L1//10, L2//10) + str(L1%10) + str(L2%10)
    else:
        return str(L1+L2)