def lingua_p(palavra):
    '''função responsável por pegar uma palavra de escolha do usuário e traduzir para a linguaguem do p pegando uma string e retornando uma string modificada'''
    p=''
    vogais='AEIOUaeiouáéíóú'
    for i in palavra:
        if i in vogais:
            p=p+i+'p'+i
        else:
            p=p+i
    return p