def inverte(frase):
    fraseminuscula=str.lower(frase)
    frasesemponto=str.replace(fraseminuscula,'.',' ')
    frasesemvirgula=str.replace(frasesemponto,',',' ')
    fraseseparada=str.split(frasesemvirgula)
    frasefinal=list.reverse(fraseseparada)
    return str.join(' ',frasefinal)