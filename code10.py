area = int(input("Digite a área em m² da parede: "))
litros_tinta = area / 3
preco_lata = 80.00
lata_tinta = 18
latas_necessarias = litros_tinta / lata_tinta

if latas_necessarias % 1 != 0:
    latas_necessarias = int(latas_necessarias) + 1
custo_total = latas_necessarias * preco_lata
print(f"Serão necessárias {latas_necessarias} latas de tinta.")
print(f"O custo total será de R$ {custo_total:.2f}.")
