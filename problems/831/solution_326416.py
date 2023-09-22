def lingua_p(palavra):
    '''recebe uma palavra e retorna-a, passando-a para a língua do p
    achei bem  divertido
    str->str'''
    p=palavra.lower()
    papalapavrapa=''
    for i in palavra:
        papalapavrapa+=i
        if i in 'aeiou':
            papalapavrapa+='p'+i
    return papalapavrapa