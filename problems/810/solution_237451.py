def inverte(frase):
    string_retira= str.replace(frase,'-',' ')
    string_retira= string_retira.replace(',',' ')
    string_retira= string_retira.replace('.',' ')
    string_retira= string_retira.replace('!',' ')
    string_retira= string_retira.replace('?',' ')
	str.lower((str.join(str.split(frase)))