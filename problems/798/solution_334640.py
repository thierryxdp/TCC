def freq_palavras(frases):
    """dada uma string, a função retorna um dicionário onde cada palavra dessa string
    seja uma chave e tenha como valor  o número de vezes que a palavra aparece"""
    frase_fragmentada=str.split(frases)
    qtde_elem=0
    dicionario={}
    for palavra in frase_fragmentada:
        qtde_elem=list.count(frase_fragmentada,palavra)
        dicionario[palavra]=qtde_elem
    return dicionario