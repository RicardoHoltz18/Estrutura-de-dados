from Pilha import Pilha
def expressao_posfixa(notacao):
    expressao = Pilha()
    for elemento in notacao:
        if elemento.isdigit() or (elemento[0] == '-' and elemento[1:].isdigit()):
            expressao.push(int(elemento))
        else:
            segundo_numero = expressao.pop()
            primeiro_numero = expressao.pop()
            if elemento == '+':
                resultado = primeiro_numero + segundo_numero
            elif elemento == '-':
                resultado = primeiro_numero - segundo_numero
            elif elemento == '*':
                resultado = primeiro_numero * segundo_numero
            elif elemento == '/':
                resultado = primeiro_numero // segundo_numero

            expressao.push(resultado)
    return expressao.pop()

expressao1= ["2", "1", "+","3","*"]
expressao2= ["4", "13", "5","/","+"]

saida1= expressao_posfixa(expressao1)
saida2= expressao_posfixa(expressao2)

print(f"Expressão 1: {expressao1}, Saída: {saida1}")
print(f"Expressão 2: {expressao2}, Saída: {saida2}")