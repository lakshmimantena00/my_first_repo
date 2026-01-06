def mutate_string(string, position, character):
    string = string[:position]+character+string[position+1:]
    return string


res=mutate_string("abcdef",2,'z')
print(res)