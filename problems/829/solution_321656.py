def soma_h(n):
    """ funcao que calcula e retorna o valro H com N termos, onde n é um int e
    dado como entrada. int-> float."""
    soma=1
    H=[]
    while soma<=n:
        if n>=soma:
            list.append(H,1/soma)
        soma+=1

    return round((sum(H)),2)