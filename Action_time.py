import pandas as pd
import csv
import shutil
import Datapreprocess

df=pd.read_csv('Cleaned_data.csv')
options=df['Disease']
options=list(options)
options_dict={}
for key in range(len(options)):
    options_dict[key]=options[key]

for key in range(len(options)):
    print(key,end=' ')
    print(":",end=' ')
    print(options_dict[key])       

print("For what disease you have to check,enter it's index: ")
print("Choose from above chart")
user_input=(int(input()))
filename=options_dict[user_input]
df1=pd.read_csv('./Disease/'+filename+'.csv')

symptoms=list(df1)

answer=[]
for key in symptoms:
    if(key=='percentage'or key=='infected'):
        continue
    print("Do you have "+key+",yes or no : ")
    user=input()
    if(user=='yes'):
        answer.append('1')
    elif(user=='no'):
        answer.append('0')
yes=0
no=0
for i in range(len(answer)):
    if(answer[i]=='1'):
        yes+=1
percentage=(yes/len(answer))*100
answer.append(percentage)

with open('./Disease/'+filename+'.csv', 'a+', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(answer)          

df2=pd.read_csv('./Disease/'+filename+'.csv')
ans=list(df2.loc[:,'percentage'])
print("You have %.2f "%ans[0],end='')
print("% "+filename)

shutil.rmtree('Disease')
