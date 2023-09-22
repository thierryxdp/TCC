def inverte(string):
    ''' funcao que inverte uma funcao dada uma string como parametro de entrada inverte a ordem destas palavras
        str --> str '''
    
    retira_ponto_final = str.replace(string,'.',' ')
    retira_ponto_interrogacao = str.replace(string,'?',' ')
    retira_ponto_exclamacao = str.replace(string,'!',' ')
    retira_virgula = str.replace(string,',',' ')
    retira_travessao = str.replace(string,'-',' ')
    
    if '?' in string:
        string1 = retira_ponto_interrogacao
        string2 = str.lower(string1)
        lista = str.split(string2,'  ')
        list.reverse(lista)
        string3 = str(lista)
        string4 = str.strip(string3,'[]')
        string5 = str.replace(string4,',',' ')
    
    
        return string5
    
    if '!' in string:
        if '-' in string:
            string1 = str.replace(retira_travessao,'!',' ')
            string2 = str.lower(string1)
            lista = str.split(string2,'  ')
            list.reverse(lista)
            string3 = str(lista)
            string4 = str.strip(string3,'[]')
            string5 = str.replace(string4,',','')
            return string5
        
        else:
            string1 = retira_ponto_exclamacao
            string2 = str.lower(string1)
            lista = str.split(string2,'  ')
            list.reverse(lista)
            string3 = str(lista)
            string4 = str.strip(string3,'[]')
            string5 = str.replace(string4,',','')
           
            return retira_ponto_exclamacao
    
    if '.' in string:
        if (',' in string) and ('-' in string):
            resultado1 = retira_virgula
            resultado2 = str.replace(resultado1,'-',' ')
            resultado3 = str.replace(resultado2,'.',' ')
            string2 = str.lower(resultado3)
            lista = str.split(string2,'  ')
            list.reverse(lista)
            string3 = str(lista)
            string4 = str.strip(string3,'[]')
            string5 = str.replace(string4,',','')
            
            return string5
        
        elif ',' in string:
            string1 = str.replace(retira_virgula,'.',' ')
            string2 = str.lower(string1)
            lista = str.split(string2,'  ')
            list.reverse(lista)
            string3 = str(lista)
            string4 = str.strip(string3,'[]')
            string5 = str.replace(string4,',','')
           
            return string5
        
        elif '-' in string:
            string1 = str.replace(retira_travessao,'.',' ')
            string2 = str.lower(string1)
            lista = str.split(string2,'  ')
            list.reverse(lista)
            string3 = str(lista)
            string4 = str.strip(string3,'[]')
            string5 = str.replace(string4,',','')
            
            return string5
        
        else:
            string1 = retira_ponto_final
            string2 = str.lower(string1)
            lista = str.split(string2,'  ')
            list.reverse(lista)
            string3 = str(lista)
            string4 = str.strip(string3,'[]')
            string5 = str.replace(string4,',','')
            
            return string5