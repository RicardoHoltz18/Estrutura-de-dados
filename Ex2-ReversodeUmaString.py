from Pilha import Pilha
def ReversodeUmaString(string):
    reverso = Pilha()
    for char in string:
        reverso.push(char)
    reversoString= ""
    while not reverso.is_empty():
        reversoString += reverso.pop()
    return reversoString

string1= "pilha"
string2= "dados"

print("O reverso da String 1 é: ", ReversodeUmaString(string1))
print("O reverso da String 2 é: ", ReversodeUmaString(string2))