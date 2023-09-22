def hashtag(s):
   
   """ Dado uma string, insere "#" no começo, no
meio e no fim dela. str -> str"""
   
   mid=len(s)//2
   return "#"+ s[:mid]+"#"+ s[mid:]+"#"