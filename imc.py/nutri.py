# Calculadora de IMC
print('Vamos calcular como está seu IMC (Índice de Massa Corporal).')

massa = float(input('Quanto você pesa (kg)? ').replace(',', '.'))
altura = float(input('Qual a sua altura (m)? ').replace(',', '.'))

# Cálculo do IMC
imc = massa / (altura ** 2)

# IMC considerado ideal
imc_ideal = 22
peso_ideal = imc_ideal * (altura ** 2)
diferenca_peso = peso_ideal - massa

print('\n📊 RESULTADO')
print(f'Seu peso atual: {massa:.1f} kg')
print(f'Sua altura: {altura:.2f} m')
print(f'Seu IMC atual é: {imc:.1f}')

# Classificação do IMC
if imc < 17:
    categoria = 'Muito abaixo do peso'
elif imc < 18.5:
    categoria = 'Abaixo do peso'
elif imc < 25:
    categoria = 'Peso ideal'
elif imc < 30:
    categoria = 'Sobrepeso'
elif imc < 35:
    categoria = 'Obesidade'
elif imc < 40:
    categoria = 'Obesidade severa'
else:
    categoria = 'Obesidade mórbida'

print(f'Classificação: {categoria}')

# Análise do peso
print('\n🎯 OBJETIVO DE PESO')
print(f'Peso saudável estimado: {peso_ideal:.1f} kg')

if diferenca_peso > 0:
    print(f'Você precisa ganhar aproximadamente {diferenca_peso:.1f} kg para atingir o peso saudável.')
elif diferenca_peso < 0:
    print(f'Você precisa perder aproximadamente {abs(diferenca_peso):.1f} kg para atingir o peso saudável.')
else:
    print('Parabéns! Você está exatamente no seu peso ideal.')

# Chamada final (fictícia)
print('\n🥗 Quer ajuda profissional?')
print('Agende uma consulta com a nutricionista Giovanna.')
print('👉 Acesse: www.nutricionistagiovanna.com (site fictício)')