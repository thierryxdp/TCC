def freq_palavras(frases):
    """funcao que recebe uma string e retorna um dicionário onde todas as palavras dessa string seja uma chave e tenha como valor o número que aparece;
    str->str"""
    dici={}
    palavras=str.split(frases)
    for palavra in palavras:
        cont=list.count(palavras, palavra)
        dici[palavra] =cont
    return dici