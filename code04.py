#medidas de um triangulo
a = float(input("Digite o valor do lado a: "))
b = float(input("Digite o valor do lado b: "))  
c = float(input("Digite o valor do lado c: "))
if a < b + c and b < a + c and c < a + b:
    print("Os valores formam um triangulo")
    if a == b == c:
        print("Triangulo Equilatero")
    elif a != b and b != c and a != c:
        print("Triangulo Escaleno")
    else:
        print("Triangulo Isosceles")