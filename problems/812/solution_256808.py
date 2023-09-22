def retira_pontuacao(frase):
    
    '''Função que irá substituir quaisquer pontuação da frase por um espaço'''
	string1 = frase.replace('!','.')
    string2 = string1.replace('?','.')
    string3 = string2.replace('/','.')
    string4 = string3.replace(':','.')
    string5 = string4.replace(',','.')
    string6 = string5.replace(';','.')
    string7 = string6.replace('[','.')
    string8 = string7.replace(']','.')
    string9 = string8.replace('-','.')
    string10 = string9.replace('...','.')
    string11 = string10.replace('""','.')
    string12 = string11.replace('(','.')
    string13 = string12.replace(')','.')
    string14 = string13.replace('.',' ')
    return string14