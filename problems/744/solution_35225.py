''' função que recebe uma string e insere o caractere "#" no inicio,
no meio e no final dela'''
'''str-> str'''
def hashtag(string):
    string = "#" + string[:len(string)//2] + "#" + string[len(string)//2:] + "#" 
      return string