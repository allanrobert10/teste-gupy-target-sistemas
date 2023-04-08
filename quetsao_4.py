# criando dicionário {estado : valor_estado}
valores = {'SP': 67836.43, 'RJ': 36678.66, 'MG': 29229.88, 'ES': 27165.48, 'Outros': 19849.53}

# somando valores da lista
valor_total = sum(valores.values())

# iterando a lista para calulcar o percentual
for estado, valor_estado in valores.items():
    percentual = (valor_estado / valor_total) * 100
    print(f"{estado}: {percentual:.2f}%")


