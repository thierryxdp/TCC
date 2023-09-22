def  posLetra(string, letra, n):

  # recebe como entrada uma string, uma letra, e um número que indica a ocorrência desejada da letra; String => Int#

    pos = -1

    qtd = 0


    for i in range(len(string)):

        if(string[i] == letra):

            qtd = qtd + 1

            if(qtd == n):

                pos = i

                break


    return pos