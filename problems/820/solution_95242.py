def posLetra(string, letra, num):
    '''Funcao que retorna a posicao de certa ocorrencia de uma letra em uma
    string, dada a string, a letra o numero da ocorrencia (str, str, int -> int)'''
    if num > str.count(string, letra):
        return 'Nao existem ocorrencias suficientes!'
    cont, ind = 1, str.index(string, letra)
    while cont < num:
        cont += 1
        ind = str.index(string[ind+1:], letra) + len(string[:ind+1])

    return ind