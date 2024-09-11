def fibonacci(n):
    #Primeiros números de Fibonacci
    a, b = 0, 1

    #Verifica se o valor informado é igual a algum dos números inciais da sequência de Fibonacci.
    if n == a or n == b:
        return f"O número {n} pertence a sequência de Fibonacci"
    
    #Gera números de Fibonacci até que o número atual seja maior ou igual a n
    while b < n:
        a, b = b, a + b

    #Verifica o valor informado é igual ao último número da sequência de Fibonacci gerada.
    if b == n:
        return f"O número {n} pertence a sequência de Fibonacci."
    else:
        return f"O número {n} não pertence a sequência de Fibonacci."

print(fibonacci(987)) 

    
