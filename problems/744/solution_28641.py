def hashtag(s):
    ''' funcao que receba uma string e insira o caractere ”#” no inicio, no meio
e no final dela '''
    meio = len(s)//2
    return '#' +s[0:meio]+ '#' +s[meio:len(s)]+ '#'