def hashtag(s):
    """ Dada uma string vamos inserir "#" no inicio, meio e final dessa string
        entrada --> str
        saida   --> str """
    inicio=s[:len(s)//2]
    meio=s[len(s)//2:]
    str_new= "#"+inicio+"#"+meio+"#"
    return str_new