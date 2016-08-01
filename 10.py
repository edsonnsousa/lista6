def main():
    palavra = raw_input("Digite a palavra:")
    palavra = palavra.lower()
    verifica_palavra(palavra)
def verifica_palavra(palavra):
    nova_palavra=""
    for i in range((len(palavra)-1),-1,-1):
        for l  in palavra[i]:
            nova_palavra=nova_palavra+l
    print nova_palavra
    if palavra == nova_palavra:
        print palavra,"Eh uma palavra palindroma "
    else:
        print palavra,"Nao eh uma palavra  palindroma"
    
if __name__ ==  "__main__":
    main()
