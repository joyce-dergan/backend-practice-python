valor_casa = int(input("Digite o valor da casa: "))
salario = int(input("Digite o salário do comprador: "))
anos = int(input("Digite em quantos anos o comprador deseja pagar: "))
prestacao = valor_casa / (anos * 12)
if prestacao > (salario * 0.3):
    print("Empréstimo negado.")
else:
    print("Empréstimo aprovado.")