def primo(n):
    primos = [2,3,5,7,11,13,17,19,23,29,31,37,41,43,47,53,59,61,67]
    i=0
    for x in primos:
        if n in primos:
            return True
        elif n/primos[i]==0:
            i+=1
            return False
        else:
            return True