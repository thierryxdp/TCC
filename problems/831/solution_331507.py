def lingua_p(palavra):
    """ Recebe uma plavra e a retorna traduzida para 
	a lingua do p; str->str
    :param palavra: Uma palavra em portugues
    :return: a palavra traduzida para língua do P."""

    vogais = "aeiouáéíóúâêîôûà"
    palavra_traduzida = ''
    palavra=str.lower(palavra)
    for letra in palavra:
		if letra in vogais:
            palavra_traduzida += letra + "p" + letra
        else:
            palavra_traduzida += letra
    return palavra_traduzida