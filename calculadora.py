def calculadora(num1, num2, operacao):
 
  if operacao == 1:
    return num1 + num2
  elif operacao == 2:
    return num1 - num2
  elif operacao == 3:
    return num1 * num2
  elif operacao == 4:
    # Verifica se o divisor é zero para evitar divisão por zero
    if num2 == 0:
      print("Divisão por zero não é permitida.")
      return 0
    else:
      return num1 / num2
  else:
    return 0

# Exemplos de uso:
resultado_soma = calculadora(5, 3, 1)
print(resultado_soma)  # Saída: 8

resultado_divisao = calculadora(10, 2, 4)
print(resultado_divisao)  # Saída: 5.0

resultado_invalido = calculadora(2, 4, 5)
print(resultado_invalido)  # Saída: 0 (operação inválida)