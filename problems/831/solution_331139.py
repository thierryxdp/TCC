def lingua_p(palavra):
    """A entrada é uma palavra em português, que está
    dentro do parâmetro e o retorno será essa palavra,
    porém em sua versão na língua p, que consiste em 
    inserir as letras pe depois de cada vogal da
    palavra, ignorando as letras maiúsculas, ou seja, 
    na tradução, todas as letras estarão minúsculas."""
    #str > str
    variavel = ''
   
    for letra in palavra:
        if letra in 'aeiou':
            variavel =  variavel + letra + 'p' + letra:
        return variavel