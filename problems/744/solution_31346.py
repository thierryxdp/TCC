def hashtag(s):
"""Retorna uma str com uma '#' no começo do elemento, no meio e no final
Str->str"""
	s=list(s)
    s.insert(0,"#")
    s.insert(len(s),"#")
    s.insert(len(s)/2,"#")
    s=''.join(s)
    return s