import webbrowser

opçoes=input("site, intitle, inurl, ext, link ou inanchor, eles contem boas combinações")
escolha=input("Qual google hacking que usar hoje?")


if escolha == "site":
    domino = input("Digite o domíno:")
    palavra =input("Digite a palavra (ex:login):")

    dork = f"site:{domino} intitle:{palavra}"

elif escolha == "intitle":
    t=input("Digite o título")
    durl =input("Digite termos dentro da url")

    dork = f"intitle:{t} inurl:{durl}"
 
elif escolha == "inurl":
    i =input("Digite o termo a ser encontrado na URL")
    dork = f"inurl:{i}"

elif escolha == "ext":
    
    dominio = input("Digite o domínio:")                                                                 
    e= input("Digite o arquivo a se localizar,exemplo:pdf,.py,.txt") 
    dork = f"site:{dominio} ext:{e}"
    


elif escolha == "link":
    l=input("Digite o link")
    dork = f"link:{l}"


elif escolha == "inanchor":
    a= input("Digite sua âncora")

    dork = f"inanchor:{a}"

   

else:
   print("Digite uma das opções!")


print("Dork", dork)

url = f"https://www.google.com/search?q={dork}"
webbrowser.open(url)




