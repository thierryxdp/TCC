# esta função que receba string e insira o caracter "#" no inicio, meio e fim
# abcd = '#'+ ab +'#'+ cd '#' -> #ab#cd#
# str-> str
def hashtag(s):
    def hashtag(s):
	return '#' + s [:len(s) //2] + '#' + s[len(s)//2:len(s)] + '#'