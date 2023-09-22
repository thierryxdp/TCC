# recebera uma string e retorne essa string no meio ou no final dela
# s
# str-> str
def hashtag(s):
    #s = s[:len(s)// 2] + s + s[-(len(s)// 2 + 1):]
    s= s[:len(s)//2] + s +  s[len(s)// 2:]
    return s