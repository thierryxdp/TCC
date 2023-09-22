def substitui(s,x,i):
    '''Função que retorna a palavra dada por s, substituindo a letra da 
    posição dada pelo número inteiro i pelo caractere x.'''
    nome = str(s)
    return nome[:int(i)] + str(x) + nome[int(i)+1:]