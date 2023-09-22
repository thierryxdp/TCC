def posLetra(string, letra, num):
    '''Funcao que retorna a posição de certa ocorrencia de uma letra em uma
    string, dada a string, a letra o numero da ocorrencia (str, str, int ->)'''
    if num > str.count(string, letra):
        return '-1'
    cont, ind = 1, str.index(string, letra)
    while cont < num:
        cont += 1
        ind = str.index(string[ind+1:], letra) + len(string[:ind+1])
        
    return ind
#A função em como objetivo me retornar uma ocorrencia
#Sendo assim, ela me retorna a posição da str
#Para q tal coisa aconteça eu usei o if num > str.count(string, letra):
#e ele me retorna -1, se a frase estiver nessas condições
#O método index me retorna o índice do elemento especificado em minh lista.
#Ele suporta tres argumentos
#O len conta o numero de caracteres