def main():
    hora= raw_input("Digite as horas(XX:XX:XX):")
    converte(hora)
def converte(hora):
    nova_hora = hora.split(":")

    print "%s horas, %s minutos,%s segundos"%(nova_hora[0],nova_hora[1],nova_hora[2])


if __name__ ==  "__main__":
    main()
