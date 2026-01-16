salario = float(input("Digite o salário do funcionário: "))
if salario <= 1500:
    aumento = salario * 0.15
    novo_salario = salario + aumento
    print(f"Novo salário com aumento de 15%: R$ {novo_salario:.2f}")
elif salario > 1500:
    aumento = salario * 0.10
    novo_salario = salario + aumento
    print(f"Novo salário com aumento de 10%: R$ {novo_salario:.2f}")