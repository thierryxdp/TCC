def lingua_p(string):
    consoantes = 'qwrtypsdfghjklçzxcvbnm'
    string_resultado = ''
    for i in range(len(string)):
        if string[i].lower() in consoantes):
            string_resultado+= string[i].lower()
        else:
            string_resultado+= string[i].lower()+'p'+string[i].lower()
    return string_resultado