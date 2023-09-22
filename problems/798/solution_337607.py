def freq_palavras(frases):
    
    """
    str--->dict
    Usa-se o comando str.split para separar as strings em uma lista com
    cada uma(ao inves de uma string inteira apenas).Isso é feito pra que
    se possa contar quantas vezes cada palavra aparece na frase, com o 
    comando count. Assim, se monta o dicionario igualando o valor obtido
    no count com cada string.
    """
    dicio={}
    
    lista=frases.split(' ')
    
    for i in range(len(lista)):
        x=lista.count(lista[i])
        dicio[lista[i]]=x

    return dicio