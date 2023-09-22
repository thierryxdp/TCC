def primo(num):

    for dado in range(1, num+1):

        for x in range(2, dado):

            if dado % x == 0:

                return True
            else:

                return False