def hashtag(s):
	'''#Esta função recebe uma palavra e retorna esta mesma palavra
	com o caractere "#" no ínicio, no meio e no final dela.
	str-> str'''

	s1=(len(s))//2
	s2=s[:s1]
	s3=s[s1:]
	
    return ('#'+s2+'#'+s3+'#')