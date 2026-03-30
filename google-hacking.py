import webbrowser

opçoes=input("site, intitle, inurl, ext, link ou inanchor, alguns contem boas combinações para uma busca completa")
escolha=input("Qual google hacking que usar hoje?")


if escolha == "site":
    domino = input("Digite o domíno:")
    palavra =input("Digite um título pra página (ex:login):")
    text    =input("Digite um texto que esteja dentro do site")
    dork = f"site:{domino} | intitle:{palavra} | intext:{text}"

elif escolha == "intitle":
    t=input("Digite o título")
    durl =input("Digite termos dentro da url")
    text1    =input("Digite um texto que esteja dentro do site")
    dork = f"intitle:{t} intext:{text1} | inurl:{durl}"
 
elif escolha == "inurl":
    i =input(" Digite o termo a ser encontrado na URL")
    i2 =input(" Digite o site 1")
    i3 =input(" Digite o site 2")
   
    dork = f"inurl:{i} | site:{i2} | site:{i3}"

elif escolha == "ext":
    
    dominio = input("Digite o domínio:")                                                                 
    e= input("Digite o arquivo a se localizar,exemplo:pdf,.py,.txt") 
    dork = f"site:{dominio} | ext:{e}"
    


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




