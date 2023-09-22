def hashtag(string):
    '''funcao com '#' no inicio, meio e final dela'''
    string= input("string:")
    strint= "#"+string+"#"
    meio= len(string)//2
    string=string[:meio]+"#"+string
      return (string)