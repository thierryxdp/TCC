def lingua_p(palavra):
    '''Função que recebe uma palavra e retorna a palavra traduzida para língua do P;
    str -> str'''
    palavra = palavra.lower()
    lista = []
    for letra in palavra:
        if letra in "aeiouAEIOUáéíóúãõô":
            lista += [letra] + ['p'] + [letra]
        else:
            lista += [letra]
        
    return "".join(lista)