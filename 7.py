def main():
    verbo=raw_input("Verbo: ")
    verbo= verbo.lower()
    print verbo
    verbo_f(verbo)
def verbo_f(verbo):
	novo_verbo= verbo[0:len(verbo)-2]
	novo_verbo = novo_verbo+"o"
	print novo_verbo
    	
if __name__== "__main__":
    main()