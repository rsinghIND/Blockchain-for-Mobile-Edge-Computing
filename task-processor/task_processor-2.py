import os
import pandas as pd
from random import randrange
import datetime

print("BEGIN")

while(1):
    if(os.path.isfile("tasks/workload.csv")):
        print("Found")
        break;
df = pd.read_csv('tasks/workload.csv', index_col=False,delim_whitespace=True)
pd.DataFrame(df.sum(), columns=['sum']).to_csv("result_1.csv")
os.system('sshpass -p "tafraliang" scp -vr result_1.csv kalikho@172.16.117.17:/home/kalikho/icbc/outputs/')

while(1):
    if(os.path.isfile("tasks/result_1_verification.csv")):
        print("===")
        print(datetime.datetime.now())
        print("Found :: result_1_verification.csv")
        df = pd.read_csv('tasks/result_1_verification.csv', index_col=False,delim_whitespace=True)
        pd.DataFrame(df.sum(), columns=['sum']).to_csv("tasks/result_2_1.csv")
        os.system('sshpass -p "tafraliang" scp -vr tasks/result_2_1.csv kalikho@172.16.117.17:/home/kalikho/icbc/verification_output/')
        print(datetime.datetime.now())
        print("Sent verification for Task 1")
        os.remove("tasks/result_1_verification.csv")

    elif(os.path.isfile("tasks/result_3_verification.csv")):
        print("Found :: tasks/result_3_verification.csv")
        print("===")
        print(datetime.datetime.now())
        df = pd.read_csv('tasks/result_3_verification.csv', index_col=False,delim_whitespace=True)
        pd.DataFrame(df.sum(), columns=['sum']).to_csv("tasks/result_2_3.csv")
        os.system('sshpass -p "tafraliang" scp -vr tasks/result_2_3.csv kalikho@172.16.117.17:/home/kalikho/icbc/verification_output/')
        print(datetime.datetime.now())
        print("Sent verification for Task 3")
        os.remove("tasks/result_3_verification.csv")

    elif(os.path.isfile("tasks/result_4_verification.csv")):
        print("===")
        print(datetime.datetime.now())
        print("Found :: tasks/result_4_verification.csv")
        df = pd.read_csv('tasks/result_4_verification.csv', index_col=False,delim_whitespace=True)
        pd.DataFrame(df.sum(), columns=['sum']).to_csv("tasks/result_2_4.csv")
        os.system('sshpass -p "tafraliang" scp -vr tasks/result_2_4.csv kalikho@172.16.117.17:/home/kalikho/icbc/verification_output/')
        print(datetime.datetime.now())
        print("Sent verification for Task 4")
        os.remove("tasks/result_4_verification.csv")
