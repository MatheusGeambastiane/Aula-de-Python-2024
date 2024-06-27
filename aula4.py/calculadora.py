numero1 = float(input("Digite o primeiro número: "))
operacao = input("Digite a operação (+, -, *, /): ")
numero2 = float(input("Digite o segundo número: "))

match operacao:
    case "+":
        resultado = numero1 + numero2
        print(f"O resultado de {numero1} + {numero2} é: {resultado}")
    case "-":
        resultado = numero1 - numero2
        print(f"O resultado de {numero1} - {numero2} é: {resultado}")
    case "*":
        resultado = numero1 * numero2
        print(f"O resultado de {numero1} * {numero2} é: {resultado}")
    case "/":
        if numero2 != 0:
            resultado = numero1 / numero2
            print(f"O resultado de {numero1} / {numero2} é: {resultado}")
        else:
            print("Erro: Divisão por zero não é permitida.")
    case _:
        print("Operação inválida. Por favor, use uma das seguintes operações: +, -, *, /")
