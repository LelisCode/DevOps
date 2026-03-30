import webbrowser

opçoes=input("site, intitle, inurl, ext, link ou inanchor, alguns contêm boas combinações para uma busca completa:")
escolha=input("Qual google hacking que usar hoje?")


if escolha == "site":
    site = input("Digite o site:")
    title =input("Digite um título pra página:")
    text    =input("Digite um texto que esteja dentro do site:")
    dork = f"site:{site} | intitle:{title} | intext:{text}"

elif escolha == "intitle":
    t   =input("Digite o título:")
    text1    =input("Digite um texto que esteja dentro do site:")
    dork = f"intitle:{t} intext:{text1}"
 
elif escolha == "inurl":
    i =input(" Digite o termo a ser encontrado na URL:")
    i2 =input(" Digite o site 1:")
    i3 =input(" Digite o site 2:")
    t =input("Digite um titulo para página")
    dork = f"(site:{i2} | site:{i3}) | inurl:{i} | intitle: {t} "

elif escolha == "ext":
    
    site = input("Digite o site 1 :")   
    site2 = input("Digite o site 2 :")
    e= input("Digite o arquivo a se localizar,exemplo:pdf,.py,.txt:") 
    dork = f"site:{site} | site:{site2} | ext:{e}"
    


elif escolha == "link":
    l=input("Digite o link:")
    dork = f"link:{l}"


elif escolha == "inanchor":
    a= input("Digite sua âncora:")

    dork = f"inanchor:{a}"

   

else:
   print("Digite uma das opções!:")


print("Dork", dork)

url = f"https://www.google.com/search?q={dork}"
webbrowser.open(url)




