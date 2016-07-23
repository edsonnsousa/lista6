def main():
    frase = raw_input("Frase:")
    duplicar(frase)
    
def duplicar(frase):
    nova_frase=""
    for letra in frase:
        nova_frase= nova_frase+letra+letra
    print nova_frase,
    
if __name__ == "__main__":
    main()
