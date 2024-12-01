import pandas


fails = pandas.read_excel("description.xlsx", sheet_name="LookupAREA")
inf_list = fails.values.tolist()


get_inf=input('Kāds reģions? ')


reg_id=0


for row in inf_list:
    if row[1]==get_inf:
        reg_id=row[0]
        break
print(reg_id)


if reg_id==0:
    print('Reģions nav atrasts')
    exit()


Data=[]
csv=open('data.csv','r')  
for line in csv:
       Data.append(line.rstrip().split(','))


Count=[]
for line in Data:
     if line[1]==reg_id:
          Count.append(int(line[3]))


print(sum(Count))