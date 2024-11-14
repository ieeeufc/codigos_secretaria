import pandas as pd # Pandas é uma biblioteca usada para manipulação de dados com planilhas, para instalá-la abra o prompt de comando e digite: pip install pandas

# Para usar o código é bem simples, baixe e copie o endereço da planilha 'Registro Reuniões.xlsx' do Drive do Ramo (Meu Drive > 1. Ramo Estudantil IEEE > 1. Comitês > Secretaria > Gerenciamento do membros > Ausência reuniões)

sheet = str(input("Digite o endereço da planilha Excel: \n")) # Pegar o endereço da planilha que será usada pelo pandas

if '"' in sheet: # Retira as aspas (") do endereço para o pandas reconhecer o documento
    sheet = sheet.replace('"', "")

df = pd.read_excel(sheet, engine='openpyxl') # Cria um DataFrame da planilha

differents_dates = df['Data'].unique() # Cria uma lista com a data de cada reunião
differents_names = df['Nome'].unique() # Cria uma lista com nome de cada membro
differents_names.sort() # Organiza a lista dos membros em ordem alfabética

def question(): # Texto com as opções
    value = input('\nEscolha uma das opções abaixo para visualizar ─ escreva seu respectivo número: \n \n 1. Frequência em uma reunião; \n 2. Ranking com frequência das reuniões; \n 3. Frequência de um membro; \n 4. Ranking com frequência dos membros. \n \n')
    if value == '1':
        option1()
        finish() 
    elif value == '2':
        option2()
        finish()
    elif value == '3':
        option3()
        finish()
    elif value == '4':
        option4()
        finish()
    else:
        print('Isso não é uma opção! Sessão finalizada.')


def option1(): # Frequência em uma reunião
    print('')
    for i in range(len(differents_dates)): # Printa cada linha
        print('{}. {}'.format(i+1, differents_dates[i]))

    num_meeting = int(input('\nQual dessas reuniões você quer visualizar? \n'))

    specific_date = df[df['Data'] == differents_dates[num_meeting - 1]] # Data

    total_people = len(specific_date) # Quantidade total de pessoas

    specific_date_on = df[(df['Data'] == differents_dates[num_meeting - 1]) & (df['Presença'] == 1)] # Filtra quem estava presente

    num_attend_spec_date = len(specific_date_on) # Quantidade de membros presentes

    frequency = round(num_attend_spec_date / total_people * 100, 2) # Porcentagem

    print('\n ', specific_date)
    print('\nA presença na reunião do dia {} foi de {}%. \n '.format(differents_dates[num_meeting - 1], frequency))


def option2(): # Ranking com frequência das reuniões

    meetings = []

    for i in range(len(differents_dates)): # Adiciona um valor na lista com data e frequência
        total = len(df[df['Data'] == differents_dates[i]])
        on = len(df[(df['Data'] == differents_dates[i]) & (df['Presença'] == 1)])
        frequency = round(on/total*100, 2)
        meetings.append([differents_dates[i], '{}%'.format(frequency)])

    meetings_df = pd.DataFrame(meetings, columns = ['Reunião', 'Frequência']) # Cria um DataFrame com a lista meetings

    meetings_df = meetings_df.sort_values(by=['Frequência'], ascending=False) # Muda a ordem da coluna frequência para decrescente
    
    meetings_df.index = range(1, len(meetings_df) + 1) # Muda o início da contagem do índice para 1
    
    print(meetings_df)


def option3(): # Frequência de um membro
    print('')
    for i in range(len(differents_names)): # Printa o nome de cada membro
        print('{}. {}'.format(i+1, differents_names[i]))

    num_member = int(input('\nQual desses membros você quer visualizar? \n'))

    specific_member = df[df['Nome'] == differents_names[num_member - 1]] # Separa as linhas com o nome do membro em específico

    total_meetings = len(specific_member) # Total reuniões ausentes e presentes

    meeting_on = len(df[(df['Nome'] == differents_names[num_member - 1]) & (df['Presença'] == 1)]) # Reuniões presentes

    frequency = round(meeting_on / total_meetings * 100, 2) # Porcentagem

    print('\n ', specific_member)

    if differents_names[num_member - 1] == 'Cleibo Júnior': # Recompensa do programador :D
        print('\nA frequência do admirável {} nas reuniões é de {}% de um total de {} reuniões.'.format(differents_names[num_member - 1], frequency, total_meetings))
    else:
        print('\nA frequência de {} nas reuniões é de {}% de um total de {} reuniões.'.format(differents_names[num_member - 1], frequency, total_meetings))  


def option4(): # Ranking com frequência dos membros
    members = []
    total_in_meetings = {}
    for i in range(len(differents_names)): # Adiciona um valor na lista com nome e frequência
        total = len(df[df['Nome'] == differents_names[i]]) # Total de reuniões presentes e ausentes
        total_in_meetings[differents_names[i]] = total # Esqueci
        on = len(df[(df['Nome'] == differents_names[i]) & (df['Presença']==1)]) # Reuniões presentes
        frequency = round(on / total * 100, 2)
        members.append([differents_names[i], '{}'.format(frequency), on])

    members_df = pd.DataFrame(members, columns=['Nome', 'Frequência', 'Proporção']) # Cria um DataFrame com a lista members

    pd.set_option('display.max_rows', None) # Mostra todas as linhas do DataFrame

    # Daqui para baixo foi uma gambiarra gigante para conseguir colocar os valores das colunas Frequência e Proporção em ordem numérica descrescente com strings no meio (3.10% e 3/10)
    members_df = members_df.astype({'Frequência': float, 'Proporção': int}) # Muda o tipo das colunas

    members_df = members_df.sort_values(by=['Frequência', 'Proporção'], ascending=[False, False]) # Ordem decrescente
    
    members_df = members_df.astype({'Frequência': str, 'Proporção': str}) # Muda o tipo novamente para string, para possibilitar a adição dos caracteres não-numéricos
    
    members_df['Frequência'] = members_df['Frequência'] + '%' # Adição da %

    for j in members_df['Nome']: # Adição da / (tente entender)
        num = str(total_in_meetings[j])
        line = (members_df['Nome'] == j).idxmax()
        term = members_df.loc[members_df['Nome'] == j, 'Proporção'].values[0]
        members_df.at[line, 'Proporção'] =  term + '/' + num

    members_df.index = range(1, len(members_df) + 1) # Muda o início da contagem do índice para 1

    print('\n', members_df)


def finish(): # (Des)continuação do código
    condition1 = 's' 
    condition2 = 'n' 

    continuing = input('\nDeseja continuar visualizando os dados? (s/n)\n')

    if continuing == condition1:
        question()
    elif continuing == condition2:
        print('\nPois bem, tenha um bom dia!')
    else:
        print('\nIsso não é uma opção! Sessão finalizada.')


print(df)

question()
