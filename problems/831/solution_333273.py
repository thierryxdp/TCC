def lingua_p(palavra):
    '''Função que recebe como parâmetro uma palavra e retorna a mesma palavra traduzida para a língua do P;
    str->str'''
    palavra=str.lower(palavra)
    linguaP=str()
    for letra in palavra:
        if letra in "aeiouáéíóú":
            linguaP=linguaP+letra+"p"+letra
        else:
            linguaP=linguaP+letra
    return linguaP