# coding: utf-8

# Imports
import csv
import matplotlib.pyplot as plt

def load_file(file_name):
    """ 
        Função que le um arquivo passado como parâmetro e retorna  em uma
        lista de OrderedDict
        
        Argumentos:
        file_name: string: Nome do arquivo
        
        Retorna: list: Lista de OrderedDict que mapeia as informações de cada linha em um dicionário
    """
    print("Carregando o documento...")
    with open(file_name, "r") as file_read:
        reader = csv.DictReader(file_read)
        data_list = list(reader)
    print("Documento carregado!")
    return data_list

def print_lines(data, count):
    """ 
          Função que imprime count linhas de uma lista
          
          Argumentos:
          data: list: Lista de dados
          count: int: Número de linhas a imprimir
          
          Retorna: 
      """
    for index in range(count):
        print(data[index])

# TAREFA 3
# TODO: Crie uma função para adicionar as colunas(features) do dicionario em uma lista, na mesma ordem
def column_to_list(data, column_name):
    """ 
        Função que retorna uma lista com as colunas referenciadas pelo parâmetro column_name
        
        Argumentos:
        data: list: Lista com os dados
        column_name: string: Nome da coluna que se quer retornar

        Retorna: list: Lista com a coluna refernciada no parâmetro column_name.
    """
    column_list = []
    for sample in range(0, len(data)):
        column_list.append(data[sample][column_name])  
    return column_list

def count_gender(data_list):
    """ 
        Função que retorna uma lista com a quantidade de homens e mulheres pespectivamente
        
        Argumentos:
        data_list: list: Lista com os dados
        
        Retorna: list: Lista com quantidade de homens e mulheres respectivamente
    """
    male = 0
    female = 0
    gender_list = column_to_list(data_list, 'Gender')
    for gender in gender_list:
        if gender == 'Male':
            male += 1
        elif gender == 'Female':
            female += 1
    return [male, female]

# TAREFA 6
# TODO: Crie uma função que pegue o gênero mais popular, e retorne este gênero como uma string.
# Esperamos ver "Masculino", "Feminino", ou "Igual" como resposta.
def most_popular_gender(data_list):
    """ 
        Função que retorna o genero com a maior quantidade (mais popular)
        
        Argumentos:
        data_list: list: Lista com os dados
        
        Retorna: string: string com o genero com a maior quantidade
    """
    answer = ""
    if count_gender(data_list)[0] > count_gender(data_list)[1]:
        answer = "Masculino"
    elif count_gender(data_list)[0] < count_gender(data_list)[1]:
        answer = "Feminino"
    else:
        answer = "Igual"
    return answer

def show_chart (data, types, quantity, column, logaritmica=True, rot=90):
    """ 
        Função que gera um gráfico de barras de acordo com os parametros passados
        
        Argumentos:
        data: list: Lista com os dados
        types: list: Lista de tipos para os labels
        quantity: list: Lista com a quantidade de itens
        column: string: Nome do eixo X
        logaritmica: boolean: True para escala logaritmica
        
        Retorna: string: string com o genero com a maior quantidade
    """
    y_pos = list(range(len(types)))
    plt.bar(y_pos, quantity)
    plt.ylabel('Quantidade')
    plt.xlabel('Gênero')
    plt.xticks(y_pos, types, rotation=rot)
    plt.title('Quantidade por {}'.format(column))
    if logaritmica:
        plt.yscale('log')
    plt.show(block=True)

def count_user_types(data_list):
    """ 
        Função que retorna a quantidade de tipos de usuários

        Argumentos:
        data_list: list: Lista com os dados
        
        Retorna: list: Lista com quantidade de assinantes, clientes e Dependentes respectivamente
    """
    subscriber = 0
    customer = 0
    dependent = 0
    user_types_list = column_to_list(data_list, 'User Type')

    for user_type in user_types_list:
        if user_type == 'Subscriber':
            subscriber += 1
        elif user_type == 'Customer':
            customer += 1
        elif user_type == 'Dependent':
            dependent += 1
    return [subscriber, customer, dependent]

def calculate_trip_statistics():
    """ 
        Função que retorna o min, max, mean e median do campo trip_duration
        
        Argumentos:
        
        Retorna: list: Lista com o min, max, mean e median do campo trip_duration
    """
    trip_duration_list = column_to_list(data_list, 'Trip Duration')
    #inicializa min_trip e max_trip com o primeiro valor da lista
    min_trip = float(trip_duration_list[0])
    max_trip = float(trip_duration_list[0])
    mean_trip = 0.
    median_trip = 0.
    total_duration = 0.

    # Itera para armazenar o menor valor, maior valor e a duração total
    for trip_duration in trip_duration_list:
        if float(trip_duration) < min_trip:
            min_trip = float(trip_duration)
        if float(trip_duration) > max_trip:
            max_trip = float(trip_duration)
        total_duration +=  float(trip_duration)

    # A média é a soma dos valores dividida pelo total de itens
    mean_trip = total_duration / len(trip_duration_list)

    # Transforma a lista de durações em inteiros para poder ordenar
    trip_duration_list = [float(trip_duration) for trip_duration in trip_duration_list]

    #Ordena a lista de durações
    sorted_list = sorted(trip_duration_list)
    sorted_list_len = len(sorted_list)

    #Mediana é o valor do meio da liusta, se a quantidade for ímpar, ou a média dos dois valores do meio, caso a quantidade seja par
    if sorted_list_len % 2 == 0:
        median_trip = (sorted_list[sorted_list_len // 2] + sorted_list[sorted_list_len // 2 - 1]) / 2.0
    else:
        median_trip =  float(sorted_list[sorted_list_len // 2])
    
    return[min_trip, max_trip, mean_trip, median_trip]    

def count_column(data, column):
    """ 
        Função que retorna a quantidade de itens de um tipo da lista passada como parâmetro
        
        Argumentos:
        data: list: Lista com os dados
        column: string: Coluna que se quer contar
        
        Retorna: list: Lista com quantidade de itens do tipo informado da lista passada como parametro
    """
    itens = set()
    itenm_list = column_to_list(data_list, column)
    for item in itenm_list:
        itens.add(item)
    return itens

def count_items(column_list):
    """ 
        Função que retorna a quantidade de itens da lista passada como parâmetro
        
        Argumentos:
        data_list: list: Lista com os dados
        
        Retorna: list: Lista com quantidade de itens da lista passada como parametro
    """
    item_types = []
    count_items = []
    for column in column_list:
        if column in item_types:
             index = item_types.index(column)
             count_items[index] += 1
        else:
             item_types.append(column)
             count_items.append(1)

    return item_types, count_items

def most_popular(column_list):
    """ 
        Função que retorna o nome e a quantidade do item mais frequente da lista
        
        Argumentos:
        column_list: list: Lista com os dados
        
        Retorna: list: Lista com o nome e a quantidade do item mais frequente da lista
    """
    types, counts = count_items(column_list)
    max_item = 0;
    popular_item = ""
    for index in range(0, len(types)):
        if counts[index] > max_item:
            max_item = counts[index]
            popular_item =  types[index]
    return[popular_item, max_item]
#---------------------------

# Lê os dados como uma lista de OrderedDict que mapeia as informações de cada linha em um dicionário
data_list = load_file("chicago.csv")

# Imprime a quantidade de linhas do arquivo
print("Número de linhas: {}".format(len(data_list)))

# Imprime a primeira linha de data_list para verificar se funcionou e identificar os campos do dicionário.
print("Linha 0: ")
print_lines(data_list, 1)
input("Aperte Enter para continuar...")

# TAREFA 1
# TODO: Imprima as primeiras 20 linhas usando um loop 
print("\n\nTAREFA 1: Imprimindo as primeiras 20 amostras")
print_lines(data_list, 20)
input("Aperte Enter para continuar...")

# TAREFA 2
# TODO: Imprima o `gênero` das primeiras 20 linhas
print("\nTAREFA 2: Imprimindo o gênero das primeiras 20 amostras")
gender_list = column_to_list(data_list, "Gender")
print_lines(gender_list, 20)
input("Aperte Enter para continuar...")

# Imrime os gêneros das primeiras 20 amostras
print("\nTAREFA 3: Imprimindo a lista de gêneros das primeiras 20 amostras")
print(column_to_list(data_list, 'Gender')[:20])

# ------------ NÃO MUDE NENHUM CÓDIGO AQUI ------------
assert type(column_to_list(data_list, 'Gender')) is list, "TAREFA 3: Tipo incorreto retornado. Deveria ser uma lista."
assert len(column_to_list(data_list, 'Gender')) == 1551505, "TAREFA 3: Tamanho incorreto retornado."
assert column_to_list(data_list, 'Gender')[0] == "" and column_to_list(data_list, 'Gender')[1] == "Male", "TAREFA 3: A lista não coincide."
# -----------------------------------------------------
input("Aperte Enter para continuar...")

# TAREFA 4
# TODO: Conte cada gênero. Você não deveria usar uma função para isso.
male = 0
female = 0
gender_count = count_gender(data_list)
male = gender_count[0]
female = gender_count[1]

# Verificando o resultado
print("\nTAREFA 4: Imprimindo quantos masculinos e femininos nós encontramos")
print("Masculinos: ", male, "\nFemininos: ", female)

# ------------ NÃO MUDE NENHUM CÓDIGO AQUI ------------
assert male == 935854 and female == 298784, "TAREFA 4: A conta não bate."
# -----------------------------------------------------
input("Aperte Enter para continuar...")

# TAREFA 5
# TODO: Crie uma função para contar os gêneros. Retorne uma lista com [count_male, count_female] (exemplo: [10, 15] significa 10 Masculinos, 15 Femininos)

print("\nTAREFA 5: Imprimindo o resultado de count_gender")
print(count_gender(data_list))

# ------------ NÃO MUDE NENHUM CÓDIGO AQUI ------------
assert type(count_gender(data_list)) is list, "TAREFA 5: Tipo incorreto retornado. Deveria retornar uma lista."
assert len(count_gender(data_list)) == 2, "TAREFA 5: Tamanho incorreto retornado."
assert count_gender(data_list)[0] == 935854 and count_gender(data_list)[1] == 298784, "TAREFA 5: Resultado incorreto no retorno!"
# -----------------------------------------------------
input("Aperte Enter para continuar...")


print("\nTAREFA 6: Qual é o gênero mais popular na lista?")
print("O gênero mais popular na lista é: ", most_popular_gender(data_list))

# ------------ NÃO MUDE NENHUM CÓDIGO AQUI ------------
assert type(most_popular_gender(data_list)) is str, "TAREFA 6: Tipo incorreto no retorno. Deveria retornar uma string."
assert most_popular_gender(data_list) == "Masculino", "TAREFA 6: Resultado de retorno incorreto!"
# -----------------------------------------------------

# Cria gráfico de barra com os gêneros
types = ["Masculino", "Feminino"]
quantity = count_gender(data_list)
show_chart(data_list, types, quantity, 'Genero', False)
input("Aperte Enter para continuar...")

# TAREFA 7
# TODO: Crie um gráfico similar para user_types. 
print("\nTAREFA 7: Verifique o gráfico!")
types = ["Assinante", "Cliente", "Dependente"]
quantity = count_user_types(data_list)
show_chart(data_list, types, quantity, 'User types', True)
input("Aperte Enter para continuar...")

# TAREFA 8
# TODO: Responda a seguinte questão
male, female = count_gender(data_list)
print("\nTAREFA 8: Por que a condição a seguir é Falsa?")
print("male + female == len(data_list):", male + female == len(data_list))
answer = "Porque existem registros com gênero em branco (não informado)"
print("resposta:", answer)

# ------------ NÃO MUDE NENHUM CÓDIGO AQUI ------------
assert answer != "Escreva sua resposta aqui.", "TAREFA 8: Escreva sua própria resposta!"
# -----------------------------------------------------
input("Aperte Enter para continuar...")

# TAREFA 9
# TODO: Ache a duração de viagem Mínima, Máxima, Média, e Mediana.
# Você não deve usar funções prontas parTODO isso, como max() e min().
trip_statistics = calculate_trip_statistics()
min_trip = trip_statistics[0]
max_trip = trip_statistics[1]
mean_trip = trip_statistics[2]
median_trip = trip_statistics[3]

print("\nTAREFA 9: Imprimindo o mínimo, máximo, média, e mediana")
print("Min: ", min_trip, "Max: ", max_trip, "Média: ", mean_trip, "Mediana: ", median_trip)

# ------------ NÃO MUDE NENHUM CÓDIGO AQUI ------------
assert round(min_trip) == 60, "TAREFA 9: min_trip com resultado errado!"
assert round(max_trip) == 86338, "TAREFA 9: max_trip com resultado errado!"
assert round(mean_trip) == 940, "TAREFA 9: mean_trip com resultado errado!"
assert round(median_trip) == 670, "TAREFA 9: median_trip com resultado errado!"
# -----------------------------------------------------
input("Aperte Enter para continuar...")

# TAREFA 10
# TODO: Verifique quantos tipos de start_stations nós temos, usando set()
user_types = count_column(data_list, 'Start Station')

print("\nTAREFA 10: Imprimindo as start stations:")
print(len(user_types))
print(user_types)

# ------------ NÃO MUDE NENHUM CÓDIGO AQUI ------------
assert len(user_types) == 582, "TAREFA 10: Comprimento errado de start stations."
# -----------------------------------------------------
input("Aperte Enter para continuar...")

# TAREFA 11
# Volte e tenha certeza que você documenteou suas funções. Explique os parâmetros de entrada, a saída, e o que a função faz. Exemplo:
# def new_function(param1: int, param2: str) -> list:
"""
      Função de exemplo com anotações.
      
      Argumentos:
          param1: O primeiro parâmetro.
          param2: O segundo parâmetro.
      
      Retorna:
          Uma lista de valores x.

      """

input("Aperte Enter para continuar...")
# TAREFA 12 - Desafio! (Opcional)
# TODO: Crie uma função para contar tipos de usuários, sem definir os tipos
# para que nós possamos usar essa função com outra categoria de dados.
answer = "no"
answer = input("Você vai encarar o desafio? (yes ou no)")

if answer == "yes":
    # ------------ NÃO MUDE NENHUM CÓDIGO AQUI ------------
    column_list = column_to_list(data_list, 'Gender')
    types, counts = count_items(column_list)
    print("\nTAREFA 11: Imprimindo resultados para count_items()")
    print("Tipos:", types, "Counts:", counts)
    assert len(types) == 3, "TAREFA 11: Há 3 tipos de gênero!"
    assert sum(counts) == 1551505, "TAREFA 11: Resultado de retorno incorreto!"
    # -----------------------------------------------------
input("Aperte Enter para continuar...")

print("\nTarefa extra 1: Qual a estação de retirada de bikes mais popular?")
# TODO: Qual a estação de retirada de bikes mais popular?
column_list = column_to_list(data_list, 'Start Station')
result = most_popular(column_list)

print("Estação mais popular:", result[0] + " com {} locações".format(result[1]))
input("Aperte Enter para continuar...")

print("\nTarefa extra 2: Crie um gráfico com as 10 estações mais populares")
# TODO: Crie um gráfico com as 10 estações mais populares
column_list = column_to_list(data_list, 'Start Station')
types, counts = count_items(column_list)
station_list = list(zip(counts, types))
ordered_station_list = sorted(station_list, reverse=True)
quantity, types  = zip(*ordered_station_list)

show_chart(data_list, types[:10], quantity[:10], 'Estação inicial', True)

