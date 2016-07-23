# -*- coding: cp1252 -*-
def main():
    frase=raw_input("Frase")
    extenso(frase)
def extenso(frase):
    extensos=["zero","um","dois","tres","quatro","cinco","seis","sete","oito","nove","dez"]
    numeros = ['0','1','2','3','4','5','6','7','8','9']
    nova_frase =""
    for i in range(len(frase)):
        if frase[i] in numeros:
            for  l  in range(len(numeros)):
                if frase[i] == numeros[l]:
                    nova_frase=nova_frase+extensos[l]
        else:
            nova_frase= nova_frase+frase[i]
    print nova_frase
        
if __name__== "__main__":
    main()
