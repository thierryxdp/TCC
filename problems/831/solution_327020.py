def lingua_p(palavra):
    """Retorna a mesma palavra traduzida para a
    lingua do P, dado: uma palavra em portugues"""
    
    palavra= str.lower(palavra)
    palavra_final=''
    vogais='aáàãâeâéêiíoóôõuú'
    for i in palavra:
        palavra_final=palavra_final+1
        if i in vogais:
            palavra_final=palavra_final+'p'+i
    return palavra_final