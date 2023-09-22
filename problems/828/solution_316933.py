def primo(num):

    n = list(range(2, num+1))

    for dado in n:
        for x in range(2,dado):

        if dado % x != 0:

            return True

        else:

            return False