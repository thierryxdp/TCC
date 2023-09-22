def hashtag(s):
 	index = len(s)//2
		s = list(s)s.append("#")s.insert(index,"#")s.insert(0,"#")
			return ''.join(s)