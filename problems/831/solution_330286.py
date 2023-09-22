def lingua_p(palavra):
    vogais = 'aeiouAEIOUáéíóúâêîôûÁÉÍÓÚÂÊÎÔÛãÃ'
    traducao = ''
    for x in palavra:
        if x in vogais:
            traducao = traducao + x + 'p' + x
        else:
            traducao = traducao + x
    return traducao.lower()