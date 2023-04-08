def fibonacci(num):
    """Função que calcula a sequência de Fibonacci até o número informado."""
    fib = [0, 1]
    while fib[-1] < num:
        fib.append(fib[-1] + fib[-2])
    return fib
    
# Entrada do usuário
numero = int(input("Informe um número inteiro: "))

# Cálculo da sequência de Fibonacci
sequencia = fibonacci(numero)
print(sequencia)

# Verificação se o número informado pertence à sequência de Fibonacci
if numero in sequencia:
    print(f"O número {numero} pertence à sequência de Fibonacci.")
else:
    print(f"O número {numero} não pertence à sequência de Fibonacci.")

