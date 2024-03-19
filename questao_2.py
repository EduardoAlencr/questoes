def sequencia_fibonacci(n):
    # Inicializa a sequência com os dois primeiros números (0 e 1)
    fibonacci = [0, 1]

    # Calcula os próximos números da sequência até atingir ou ultrapassar o valor de n
    while fibonacci[-1] < n:
        proximo_numero = fibonacci[-1] + fibonacci[-2]
        fibonacci.append(proximo_numero)

    return fibonacci

def verifica_pertencimento(numero, fibonacci):
    if numero in fibonacci:
        return True
    else:
        return False

# Função principal
def principal():
    # Solicita ao usuário que insira um número
    numero = int(input("Digite um número para verificar se pertence à sequência de Fibonacci: "))

    # Calcula a sequência de Fibonacci até o número informado
    fibonacci = sequencia_fibonacci(numero)

    # Verifica se o número pertence à sequência de Fibonacci
    pertence = verifica_pertencimento(numero, fibonacci)

    if pertence:
        print(f"O número {numero} pertence à sequência de Fibonacci.")
    else:
        print(f"O número {numero} não pertence à sequência de Fibonacci.")

if __name__ == "__main__":
    principal()