# -*- coding: cp1252 -*-
def main():
    data=raw_input("Digite a data( / / )")
    data = data.split("/")
    data_mes(data)
def data_mes(data):
    meses = ['Janeiro','Fevereiro','Março','Abril','Maio','Junho','Julho','Agosto','Setembro','Outubro','Novembro','Dezembro']
    print  data[0],"de  %s de "%(meses[int(data[1])-1]),data[2]
if __name__== "__main__":
    main()
