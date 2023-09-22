#3
'''
insere consoante p+vogal apos cada vogal
string -> string
'''
def lingua_p(word):

  word = word.lower()
  newWord = str()
  
  for cha in word:
    if(cha in "aáãàâäeéêèiíîìoóõôòuúùû"):
      newWord = newWord + cha + "p" + cha
    else:
      newWord = newWord + cha
  return newWord