def primo(n):
    p = [2,3,5,7,11,13,17,19,23,29,31,37,41,43,,47,53,59,61,e]
    i=0
    for x in p:
        if n in p:
            return True
        elif n/p[i]==0:
            i+=1
            return False
        else:
            return False