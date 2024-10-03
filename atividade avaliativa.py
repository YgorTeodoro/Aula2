# Atividade 1

# Definindo duas variáveis
a = 55
b = 7
# Realizando a soma 
resultado = a + b
# Exibindo  o resultado 
print("A soma a:", resultado)

# Atividade 2
# definindo duas strings 
string1 = "Ygor "
string2 = "Teodoro "
# conectando os strings
resultado = string1 + string2
print(resultado)
# Atividade 3

# Função calcular media
def calcular_media(numeros):
    return sum(numeros) / len(numeros)
# Listas de numeros para medias
notas1 = [7, 8.5, 10]
notas2 = [6, 7.4, 8.9]
notas3 = [9, 6, 7]
notas4 = [5, 7, 9]

# Atividade 3
# Calculando medias
media1 = calcular_media(notas1)
media2 = calcular_media(notas2)
media3 = calcular_media(notas3)
#exibindo as medias
print("Média 1:", media1)
print("Média2:", media2)
print("Média3", media3)
# Calculando a media final das  três médias
media_final = calcular_media([media1, media2, media3])
# Exibindo a média final
print("Média final:", media_final)

# Atividade 4

# Função Calcular área de um retângulo
def calcular_area_retangulo(largura, altura):
    return largura * altura
largura = float(input("digite a largura do retângulo: "))
altura = float(input("digite a altura do retângulo: "))

# Calcular área
area = (largura * altura) 

# Exibindo o resultado
print(f" A área do triângulo é: {area}")