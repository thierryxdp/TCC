def inverte(retira_pontuacao(812):
    ''' funcao que inverte uma funcao dada uma string como parametro de entrada inverte a ordem destas palavras
        str --> str '''
    
    string2 = str.lower(retira_pontuacao(string))
    lista = str.split(string2,' ')
    lista1 = list.reverse(lista)
    string3 = str(lista1)
    string4 = str.strip(string3,'[]')
    string5 = str.replace(string4,',',' ')
    
    return string5