nome = input('Digite o seu nome ') # digitar o nome
print('Seja bem vindo:', nome)

num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))
operacao = input("Digite a operação (+, -, *, /): ") # escolhe o tipo de operação aritmética
if operacao == "+":
    resultado = num1 + num2
elif operacao == "-":
    resultado = num1 - num2
elif operacao == "*":
    resultado = num1 * num2
elif operacao == "/":
    resultado = num1 / num2
else:
    resultado = "Operação inválida" # informará que a operação é inválida se não for escolhida alguma operação aritmética
print('O resultado é:', resultado)
if resultado >= 50: # informará se o resultado for maior ou igual a 50
    print('Resultado é maior ou igual a 50')
elif resultado == 0 and 1: # # informará se o resultado for 0 ou 1
    print('Resultado é igual a zero ou 1')
else:
    print('Resultado é menor que 50') # se o resultado não for maios ou igual a 50, infomará que é menor que 50
if resultado >= 50 and resultado <= 100:
    print(True) # mostrará True se o resultado for entre 50 e 100
else:
    print(False) # mostrará Falso se o resultado for menor que 50 e mais que 100
val = resultado
while (val < 500): # vai fazer o loop e somar 10, enquanto val for menor que 500
  val += 50
  print(val)
for contador1 in range(int(resultado)): # pede para repetir todos os números inteiros do resultado
  print(contador1)
  if contador1 == 10: # o contador irá parar se chegar no número 10
    break
for contador2 in range(int(resultado)): # pede para repetir todos os números inteiros do resultado
  print(contador2)
  if contador2 == 20: # o contador irá parar se chegar no número 20
    break
lista = [contador1, contador2] # criada uma lista com contador1 e contador 2
print(lista)
for i, val in enumerate(lista): # irá enumerar os 2 contadores
  print(i, val)
lista.append('30')  # irá acrescer '30' ao final da lista
print(lista)
