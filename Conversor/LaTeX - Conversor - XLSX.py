import pandas as pd

list_meeting = input("Texto LaTeX com a presença dos membros: \n")

print('\n \n \n')

date = input("Qual a data da reunião (digite nesse formato --/--/----): \n")

if '/' in date:
    new_date = date.replace('/', '_')


separation = list_meeting.split(', ')

attendance = {

}

missing_term = "\\textcolor{gray}{"

n = 0

for i in separation:
    if missing_term in separation[n]:
        name_error = separation[n].replace("\\textcolor{gray}{", "")
        name = name_error.replace("}", "")
        attendance.update({name: 0})
        n += 1
    else:
        attendance.update({separation[n]: 1})
        n += 1

print('\n')

df = pd.DataFrame(list(attendance.items()), columns=['Nomes', 'Presença'])

df.insert(0, 'Data', date)

print(df, '\n')

local = input('Qual o endereço onde a planilha deve ser gerada: \n')

if "\\" in local:
    local = local.replace('\\', '\\'+'\\')

address = '{}\\Presença - {}.xlsx'.format(local, new_date)

df.to_excel(address, index=False, engine='openpyxl')

print('\nPlanilha com presença dos membros está sendo criada. \n')