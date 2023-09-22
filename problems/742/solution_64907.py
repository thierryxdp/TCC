def substitui(s,x,i):
    '''Substitui letra na posição escolhida.
    Inserir palavra entre aspas.
    str--> str'''
    parte1 = s[0:i] #pega letras da palavra começando da primeira até 1 letra antes da string i

    parte2 = s[i1:len(s)]  #pega as letras da palavra imediatamente depois da str i até o final da palavra

    return parte1 + x + parte2 #retorna a concatenação de strings