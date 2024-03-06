from Pilha import Pilha

def validacao(string):
    valida = Pilha()
    for char in string:
        if char == '(':
            valida.push(char)
        elif char == ')':
            if valida.is_empty():
                return False
            valida.pop()
    return valida.is_empty()

string_certa = "((()))"
string_errada = "(()))"

print("A primeira string está certa?" , validacao(string_certa))
print("A segunda string está certa?" , validacao(string_errada))


