def lingua_p(palavra):
    '''função que recebe como parâmetro uma palavra e 
    retorna esta mesma palavra traduzida para a língua do P
    str->str'''
    def lingua_p(palavra):
    adiciona_p=()
    palavra=str.lower(palavra)
    for i in palavra:
        if i in 'aeiou':
            adiciona_p=adiciona_p+i+'p'+i
        else:
            adiciona_p=adiciona_p+i
    return adiciona_p