def primo(num):

    n = list(range(2,num-1))

    for dado in n:

        if num % dado != 0:

            return True

        else:

            return False