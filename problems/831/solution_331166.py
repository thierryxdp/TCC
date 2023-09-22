def lingua_p(palavra):
    """Dada uma frase, a função irá alterar as vogais, adicionando um P após cada vogal
    e repetindo a própria vogal. No caso de ser uma consoante, a função não irá fazer nada.
    tipo da variável palavra: string
    tipo da saída: string"""
    string_palavra = ""
    for contador in range(len(palavra)):
        if palavra[contador] in "AEIOUaeiouáÁúÚéÉ":
            string_palavra = string_palavra + palavra[contador] + "p" + palavra[contador]
		else:
            string_palavra = string_palavra + palavra[contador]
	return string_palavra