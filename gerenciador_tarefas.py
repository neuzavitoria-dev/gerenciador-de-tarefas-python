tarefas = []

def adicionaTarefa():
    nome =     input("Nome da tarefa: ")
    categoria = input("Categoria da tarefa: ")
    prioridade = input("Prioridade (Alta, Media, Baixa): ").capitalize()
   
    nova_tarefa = {
        'nome': nome,
        'categoria': categoria,
        'prioridade': prioridade,
        'status': False
    }
    tarefas.append(nova_tarefa)
    print("Terefa adicionada com sucesso.")

def listaTarefa():
    if not tarefas:
        return "Nenhuma tarefa cadastrada."
    
    resultado = ""
    for indice, tarefa in enumerate(tarefas):
        if tarefa['status']:
            situacao = "Concluída"
        else:
            situacao = "Pendente"
        resultado += f"""
Tarefa {indice + 1}
Nome: {tarefa['nome']}
Categoria: {tarefa['categoria']}
Prioridade: {tarefa['prioridade']}
Status: {situacao}
"""  
        return resultado

def concluirTarefa():
    if not tarefas:
         return "Nenhuma tarefa cadastrada."
    for indice, tarefa in enumerate(tarefas):
        print(f"{indice + 1} - {tarefa['nome']}")

    tarefa = int(input("Digite o nùmero da tarefa que deseja concluir; "))
    indice = tarefa -1

    if 0 <= indice < len(tarefas):
        tarefas[indice]['status'] = True
        print("Tarefa marcada como concluída!")
    else:
        print("Número inválido.")

def Prioridade():
    prioridades = ("Alta", "Media", "Baixa")
    escolha = input("Escolha a prioridade (Alta, Media, Baixa): ").capitalize()

    if escolha not in prioridades:
       print("Prioridade inválida.")
       return
    
    encontrou = False
    
    for tarefa in tarefas:
        if tarefa["prioridade"] == escolha:
            print(tarefa["nome"])
            encontrou = True

    if not encontrou:
        print("Nenhuma tarefa encontrada com essa prioridade.")  

def Categoria():
    if not tarefas:
        print("Nenhuma tarefa cadastrada.")
        return
    
    categorias = set()

    for tarefa in tarefas:
        categorias.add(tarefa["categoria"])

    print("Categorias disponíveis:")
    for categoria in categorias:
        print(f"- {categoria}")

    escolha = input("Digite a categoria: ")

    if escolha not in categorias:
        print("Categoria inválida.")
        return

    for tarefa in tarefas:
        if tarefa["categoria"] == escolha:
            print(f"- {tarefa['nome']}")


while True:
    print("""
    1 - Adicionar tarefa
    2 - Ver tarefas
    3 - Marca como concluida
    4 - Filtrar prioridade
    5 - Filtrar categoria
    0 - Sair
    """)

    opcao = input("Escolha a opção que deseja: ")

    match opcao:
        case "1":
            adicionaTarefa()

        case "2":
           print(listaTarefa())

        case "3":
            concluirTarefa()

        case "4":
            Prioridade()

        case "5":
            Categoria()

        case "0":
            print("Fim do programa")
            break

        case _:
            print("Opção invàlida.")
   
    
            
    


    
    
    




    


    


