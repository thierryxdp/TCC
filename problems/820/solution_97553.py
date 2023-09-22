def posLetra(frase, letra, num):
    '''função que recebe string, letra e número e deve retornar
    a posição da letra dada sua recorrência passada (o número),
    caso haja menos recorrências que o número passado, a função 
    deve retornar -1'''
    k, lista = -1, []
    if frase.count(letra) < num:
        return -1
    else:
        for i in frase:
            k += 1
            if i == letra:
                lista.append(k)
        return lista[num]