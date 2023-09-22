def lingua_p(palavra):
    palavra=str.lower(palavra)
    palavra_final=''
    vogais='aáàãâeéêiíoóõôuú'
    for i in palavra:
        palavra_final = palavra_final+1
        if i in vogais:
            palavra_final = palavra_final + 'p' + i
    return palavra_final