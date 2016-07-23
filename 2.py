def main():
    frase= raw_input("Frase: ")
    seperar(frase)
    
def seperar(frase):
    frase = frase.split()
    for i in frase:
            print i
if __name__ == "__main__":
    main()

