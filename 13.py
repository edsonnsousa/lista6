def main():
    nome =raw_input("Nome Completo: ")
    novo_nome(nome)
def novo_nome(nome):
    novo_nome = nome.split(" ")
    ultimo_nome= novo_nome[(len(novo_nome)-1)]
    novo_nome.remove(novo_nome[(len(novo_nome)-1)])
    nome_final = ""
        
    for i in range(len(novo_nome)):
        nome_final = nome_final + novo_nome[i][0]+ "."
   
    print "%s,%s"%(ultimo_nome,nome_final)

if __name__ == "__main__":
    main()
