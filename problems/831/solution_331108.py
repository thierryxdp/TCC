def lingua_p(palavra):
    '''Função que recebe uma palabra e a cada vogal da
    palavra original identificada adiciona a letra p após a 
    vogal identificada e repete a vogal após o p.
    str ->str'''
    vogal='AEIOUÁÉÍÓÚaeiouáéíóú'
    nova_palavra=[]
    for letra in list(palavra):
        if letra in vogal:
            nova_palavra += letra+'p'+letra
        else:
            nova_palavra.append(letra)
    return ''.join(nova_palavra)