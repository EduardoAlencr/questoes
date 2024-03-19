def inverter_string(string):
    # Inicializa uma string vazia para armazenar o resultado
    string_invertida = ""

    # Percorre a string de trás para frente e concatena os caracteres na nova string
    for i in range(len(string) - 1, -1, -1):
        string_invertida += string[i]

    return string_invertida

# Exemplo de uso:
string_original = input("Digite uma string para inverter: ")
string_invertida = inverter_string(string_original)
print("String invertida:", string_invertida)