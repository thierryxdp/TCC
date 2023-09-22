def linguap(palavra):
    """Função que recebe como parâmetro uma palavra e retorna a mesma palavra traduzida para a lingua do P.
    Uma palavra traduzida para a lingua do P quando, após cada vogal da palavra original, é inserida a sequencia de letras p mais a vogal original."""
    palavra = str.lower(palavra)
    palavra_p=[]
    for letra in range(len(palavra)):
       list.append(palavra_p, palavra[letra])
       if palavra[letra] in "aeiouáéíóúàèìòùãõâêîôû":
           list.append(palavra_p,"p" + palavra[letra])
    return str.join("", palavra_p)