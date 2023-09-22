def inverte(string):
    ''' funcao que dada uma frase como parametro de entrada retorne a frase sem letras minusculas e com o sentido invertido
        str --> str '''
    retira_ponto_final = str.replace(string,'.',' ')
    retira_ponto_interrogacao = str.replace(string,'?',' ')
    retira_ponto_exclamacao = str.replace(string,'!',' ')
    retira_virgula = str.replace(string,',',' ')
    retira_travessao = str.replace(string,'-',' ')
    
    (if ',' in string) and (if '-' in string):
        resultado1 = retira_virgula
        resultado2 = str.replace(resultado1,'-',' ')
        resultado3 = str.replace(resultado2,'.',' ')
        resultado4 = str.lower(resultado3)
        resultado5 = str.reverse(resultado4)
        resultado6 = list.reverse(resultado5)
        resultado7 =