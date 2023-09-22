def primo (n):
    if n>1:
        for i in range(2, n):
            if (n%1)==0:
                print(n,"não é primo")
                break
            else:
                print(n, "é primo")
        else:
            print (n, "não é primo")