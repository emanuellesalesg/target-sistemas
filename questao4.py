faturamento_estados = {
    "SP": 67836.43,
    "RJ": 36678.66,
    "MG": 29229.88,
    "ES": 27165.48,
    "Outros": 19849.53
}

#Calcula o faturamento total mensal
faturamento_total = sum(faturamento_estados.values())

#Calcula o percentual de representação de cada estado
percentual_representacao = {
    estado: (valor / faturamento_total) * 100 for estado, valor in faturamento_estados.items()
}

#Mostra o percentual de representação de cada estado
for estado, percentual in percentual_representacao.items():
    print(f"{estado}: {percentual:.2f}%")


