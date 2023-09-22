def lingua_p(palavra):
    '''
    Funcao que retorna uma palavra na lingua do P,
    após tal palavra ser psota em protugues na entrada
    da função, a qual insere a letra p mais uma vogal da palavra logo depois
    de tal vogal da aplavra original
    Ex.: entao -> epentapaopo
    str -> str
    '''
    vogal=str.lower(palavra)
    contador=0
    traducao_linguaP=''
    while contador<len(vogal):
        if vogal[contador] in "aeiouáéú":
            traducao_linguaP=traducao_linguaP+vogal[contador]+"p"+vogal[contador]
        else:
            traducao_linguaP=traducao_linguaP+vogal[contador]
        contador=contador+1
    return traducao_linguaP