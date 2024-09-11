import json

# Carrega o arquivo json localizado na pasta dados
with open("dados/dados.json", "r") as file:
    faturamento = json.load(file)

# Filtra os dias com faturamento > 0
faturamento_validos = [dia["valor"] for dia in faturamento if dia["valor"] > 0]

menor_valor = min(faturamento_validos)
maior_valor = max(faturamento_validos)
media_mensal = sum(faturamento_validos) / len(faturamento_validos)

#Conta dias com faturamento acima da média
dias_acima_da_media = sum(1 for valor in faturamento_validos if valor > media_mensal)

print(f"Menor valor de faturamento: {menor_valor}")
print(f"Maior valor de faturamento: {maior_valor}")
print(f"Dias com faturamento acima da média: {dias_acima_da_media}")
