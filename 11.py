def main():
    texto = raw_input("Digite o texto: ")
    conta_palavras(texto)
def conta_palavras(texto):
    total = texto.split(" ")
    print "O texto digitado  possui %d palavras"%(len(total))
if __name__ == "__main__":
    main()
