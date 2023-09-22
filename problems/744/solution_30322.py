'''funçao que, fornecida uma string (s), insere o caracter '#'
no inicio, no meio e no final dela
str -> str'''
def hashtag(s):
    	s = "#" + s[:len(s)//2] + "#" + [len(s)//2:] + "#":
        	return s