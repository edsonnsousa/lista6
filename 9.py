def main():
    usuario= raw_input("Usuario: ")
    senha= raw_input("Digite a senha: ")
    for i in range(len(senha)):
        print "*",
    print "\n"
    verifica(senha,usuario)
def verifica(senha,usuario):
    confirma_senha=raw_input("Digite a senha Novamente: ")
    if confirma_senha == senha:
        print usuario,"Senha confirmada"
    else:
        print "Senha incorreta"
        verifica(senha,usuario)

if __name__ ==  "__main__":
    main()
