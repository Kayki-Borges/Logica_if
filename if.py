velocidade = float(input("Digite a velocidade do carro:"))
if velocidade >80 :
    print("sua velocidade é de {}, você foi multado, e sua multa vai ser de 7 reais por quilometro você vai pagar {}".format(velocidade,(velocidade-80)*7))
else:
    print("Sua velocidade é de {}, você esta no limite e não foi multado".format(velocidade))