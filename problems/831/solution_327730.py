def lingua_p(palavra):
    '''função que recebe como parâmetro uma palavra e 
    retorna esta mesma palavra traduzida para a língua do P
    str->str'''
    adiciona_p=()
    palavra=str.lower(palavra)
    for i in palavra:
        if palavra[i]=='aeiou':
            adiciona_p=adiciona_p+'aeiou'
        else:
            i=i+1
            adiciona_p=adiciona_p+palavra[i]
        i=i+1
    return adiciona_p