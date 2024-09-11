def inverte_string(texto):
    texto_invertido = ""

    #Itera do último ao primeiro caractere da string
    for i in range(len(texto) -1, -1, -1):
        texto_invertido += texto[i]
    return texto_invertido

texto_exemplo = "Invertendo o texto"
print(inverte_string(texto_exemplo))