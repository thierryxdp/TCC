def hashtag (input):
string = '#'+string+'#'
meio = len(string)//2
string = string[:meio] + '#' + string[meio:]

return string