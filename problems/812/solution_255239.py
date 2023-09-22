def retira_pontuacao(frases):
    '''comente'''
    string=frases
    string1= str.replace(frases,'-',' ')
    string2= str.replace(string1,',',' ')
    string3= str.replace(string2,'!',' ')
    string4= str.replace(string3,'?',' ')
    string5= str.replace(string4,'.',' ')
    return string