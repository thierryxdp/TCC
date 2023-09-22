def lingua_p(palavra):
    """Função que recebe como parâmetro uma palavra (em português) e retorne esta mesma palavra traduzida para a língua do P. Uma palavra foi traduzida para a língua do P quando, após cada vogal da palavra original, é inserida a sequência de letras 'p' mais a vogal original.
string -> string"""
    letra=list(palavra)
    for i in letra:
      cont=0
      for vogal in letra:
         if vogal in 'aeiouáéíóú' and letra[cont]==vogal:
           letra[cont]=letra[cont]+'p'+vogal
         cont+=1
    return str.join('',letra)