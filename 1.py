def  main():
    frase = raw_input("Frase: ")
    frase = frase.lower()
    inverte(frase)
    
def inverte(frase):
    vogais=['a','e','i','o','u']
    for i in frase:
        if i not in vogais:
            frase=frase.replace(i,"#")
        else:
             pass
    frase=frase[::-1]
    print frase
    
if __name__=="__main__":
    main()
