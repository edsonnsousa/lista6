def main():
    frase = raw_input("Frase: ")
    retira(frase)
def retira(frase):
    frase = frase.replace(" ","")
    print frase
if __name__ ==  "__main__":
    main()
