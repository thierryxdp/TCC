def primo (n):
    if n>1:
        for i in range(2, n):
            if (n%1)==0:
                return True
                break
            else:
                return False
        else:
            return True