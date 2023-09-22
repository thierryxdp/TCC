def hastag(string):
    ''' recebe uma string e retorna a string com # no inicio, no meio
    e no fim dela, EX: abcd = #ab#cd# '''
    tamanhoString = len(string)
    fatia1 = string[0:2]
    fatia2 = string[2:]
    resultado = '#' + fatia1 + '#' + fatia2 + '#'
    if tamanhoString > 1 and tamanhoString <=3:
        fatia1 = string[0]
        fatia2 = string[1:]
        resultado = '#' + fatia1 + '#' + fatia2 + '#'
    elif tamanhoString > 3 and tamanhoString <= 5:
        fatia1 = string[0:2]
        fatia2 = string[2:]
        resultado = '#' + fatia1 + '#' + fatia2 + '#'
    elif tamanhoString > 5 and tamanhoString <= 7:
        fatia1 = string[0:3]
        fatia2 = string[3:]
        resultado = '#' + fatia1 + '#' + fatia2 + '#'
    elif tamanhoString > 7 and tamanhoString <= 9:
        fatia1 = string[0:4]
        fatia2 = string[4:]
        resultado = '#' + fatia1 + '#' + fatia2 + '#'
    elif tamanhoString > 9 and tamanhoString <= 11:
        fatia1 = string[0:5]
        fatia2 = string[5:]
        resultado = '#' + fatia1 + '#' + fatia2 + '#'
    elif tamanhoString > 11 and tamanhoString <= 13:
        fatia1 = string[0:6]
        fatia2 = string[6:]
        resultado = '#' + fatia1 + '#' + fatia2 + '#'
    return str(resultado)