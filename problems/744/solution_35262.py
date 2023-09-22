def hashtag(s):
    '''funcao que recebe uma string e insira o caractere ”#” no inıcio, no meio
	e no final str -> str'''
    total = len(s)//2 
    parte1 = s[:total]
    parte2 = s[total:]
    return str('#') + str(parte1)+ str('#') + str(parte2) + str('#')