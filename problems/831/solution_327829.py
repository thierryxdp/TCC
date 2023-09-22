def lingua_p(palavra:str)->str:
    """ A função recebe como parâmetro uma palavra em português e retorna a palavra traduzida para a lígua do P. Essa tradução é a seguinte: após cada vogal dessa palavra é inserida a sequência de letras p, mais a vogal original."""
    palavra_ligua_p = ''
    for indice in range(len(palavra)):
        if palavra[indice] in 'aáeéiíoóuúãõ':
            palavra_ligua_p += palavra[indice] + 'p' + palavra[indice]
        else:
            palavra_ligua_p += palavra[indice]
    return palavra_ligua_p