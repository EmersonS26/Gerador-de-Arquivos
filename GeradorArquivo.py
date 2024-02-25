import csv
import os

while True:
    print("BEM VINDO!\nO criador de arquivos está em execução:\n ")
    v = input("Digite valores para o documento:[X-excluir um arquivo], [R-ler], [A-acrescentar], [W-criar e sobrescrever arquivo csv] ou [E-exit] para sair: ")
    
    if v == "E":
        exit()
    
    if v == "A": #adiciona elementos a pasta existente
        nomePasta = input("Digite o nome da sua pasta: ")
        elementosArquivo = input(f"Escreva os elementos que deseja adicionar no arquivo {nomePasta}: ")
        with open(f'{nomePasta}.csv','a',encoding='utf-8')as novoArquivo:
            escrever = csv.writer(novoArquivo)
            escrever.writerow([f"{elementosArquivo}"])
            print(f"Elementos da pasta {nomePasta}, arquivo {escrever} foram acrescentados com sucesso!")
    elif v == "R": #Lê o que tem dentro de uma pasta
        nomePasta = input("Digite o nome da sua pasta: ")
        with open(f"{nomePasta}")as pastinha:
            for x in csv.reader(pastinha):
                print(x)
    elif v == "W": #Cria e sobrescreve uma pasta/arquivo
        nomePasta = input("Digite o nome da sua pasta: ")
        print(f"Pasta {nomePasta} criada com sucesso: ")
        elementosArquivo = input(f"Adicionar elemento(s) na pasta {nomePasta}: [S-sim] | [N-sair] : ")
        if elementosArquivo == "N":
            with open (f"{nomePasta}.csv","w", encoding="utf-8")as sobres:
                valor2 = csv.writer(sobres)
                valor2.writerow([f"{elementosArquivo}"])
                print(f"Pasta {nomePasta} foi criado com sucesso, encerrando operação... ")
                exit() #cria uma pasta/arquivo e finaliza a operação
        if elementosArquivo == "S":
            elementosArquivo = input("Escreva os elemento(s) que deseja adicionar no arquivo: ")
            with open(f'{nomePasta}.csv','a',encoding='utf-8')as sobre:
                valor2 = csv.writer(sobre)
                valor2.writerow([f"{elementosArquivo}"])
                print(f"Elementos da pasta {nomePasta} foram adicionados com sucesso!")
                menu = input(" documento:[R-ler], [A-adicionar elementos], [W-criar e/ou sobrescrever arquivo csv] [S-sair] ")
                if menu == "A":
                    elementosArquivo = input("Escreva os elementos que deseja adicionar no arquivo: ")
                    with open(f'{nomePasta}.csv','a',encoding='utf-8')as sobre:
                        valor2 = csv.writer(sobre)
                        valor2.writerow([f"{elementosArquivo}"])
                        print(f"Elementos da pasta {nomePasta} foram adicionados com sucesso!")
                if menu == "R":
                    nomePasta = input("Digite o nome da sua pasta: ")
                    with open(f"{nomePasta}.csv", "r", encoding="utf-8")as leitura:
                        ler = csv.reader(leitura)
                        print(f"Abrindo a pasta {ler}")
                if menu == "W":
                    nomePasta = input("Digite o nome da sua pasta: ")
                    elementosArquivo = input("Escreva os elementos que deseja adicionar/substituir no arquivo: ")
                    with open (f"{nomePasta}.csv","w", encoding="utf-8")as sobres:
                        valor2 = csv.writer(sobres)
                        valor2.writerow([f"{elementosArquivo}"])
                        print(f"Pasta {nomePasta} foi alterada com sucesso:\n ")
                        print(F"Elementos da pasta antiga foram substituidos...\n Itens acrescentados: {elementosArquivo}")
                        
     # Tratamento de erro para excluir o arquivo/pasta           
    try:
        if v == "X":
        # Exclui o arquivo CSV
            nomePasta = input("Digite o nome da sua pasta: ")
            if os.path.exists(f"{nomePasta}"):
                os.remove(f"{nomePasta}")
                print(f"O arquivo {nomePasta} foi excluído permanentemente com sucesso!")
            else:
                print(f"O arquivo {nomePasta} não existe.")
                break
    except Exception as e:
        print(f"Erro ao excluir o arquivo: {e}")              
            
         
        