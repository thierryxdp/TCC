def hashtag (string):
hashtag = '#'+string+'#'
meio = len(string)//2
string = string[:meio] + '#' + string[meio:]

return string