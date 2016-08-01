def main():
    nome =raw_input("Nome Completo: ")
    novo_nome(nome)
def novo_nome(nome):
    novo_nome = nome.split(" ")
    print "%s/%s"%(novo_nome[(len(novo_nome)-1)],novo_nome[0])
    
if __name__ == "__main__":
    main()
