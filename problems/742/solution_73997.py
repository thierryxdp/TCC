def substitui(s,x,i):
    '''Função que retorna a palavra dada por s, substituindo a posição dada 
    pelo número inteiro i pelo caractere x.'''
    nome1 = str(s)
    return nome1[:int(i)] + str(x) + nome1[int(i)+1:]