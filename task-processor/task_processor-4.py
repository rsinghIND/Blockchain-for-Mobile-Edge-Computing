import os
import pandas as pd
from random import randrange
import datetime

print("BEGIN")

while(1):
    if(os.path.isfile("tasks/workload.csv")):
        print("Found")
        break;
df = pd.read_csv('tasks/workload.csv', index_col=False)
pd.DataFrame(df.sum(), columns=['sum']).to_csv("result_1.csv")
os.system('sshpass -p "tafraliang" scp -vr result_1.csv kalikho@172.16.117.17:/home/kalikho/icbc/outputs/')

while(1):
    if(os.path.isfile("tasks/result_2_verification.csv")):
        print("===")
        print(datetime.datetime.now())
        print("Found :: tasks/result_2_verification.csv and now Computing ... ")
        df = pd.read_csv('tasks/result_2_verification.csv', index_col=False,delim_whitespace=True)
        pd.DataFrame(df.sum(), columns=['sum']).to_csv("tasks/result_4_2.csv")
        os.system('sshpass -p "tafraliang" scp -vr tasks/result_4_2.csv kalikho@172.16.117.17:/home/kalikho/icbc/verification_output/')
        print(datetime.datetime.now())
        print("Sent verification for Task 2")
        print("===")
        os.remove("tasks/result_2_verification.csv")

    elif(os.path.isfile("tasks/result_3_verification.csv")):
        print("===")
        print(datetime.datetime.now())
        print("Found :: tasks/result_3_verification.csv and now Computing ... ")
        df = pd.read_csv('tasks/result_3_verification.csv', index_col=False,delim_whitespace=True)
        pd.DataFrame(df.sum(), columns=['sum']).to_csv("tasks/result_4_3.csv")
        os.system('sshpass -p "tafraliang" scp -vr tasks/result_4_3.csv kalikho@172.16.117.17:/home/kalikho/icbc/verification_output/')
        print(datetime.datetime.now())
        print("Sent verification for Task 3")
        print("===")
        os.remove("tasks/result_3_verification.csv")

    elif(os.path.isfile("tasks/result_1_verification.csv")):
        print("===")
        print(datetime.datetime.now())
        print("Found :: tasks/result_1_verification.csv and now Computing ... ")
        df = pd.read_csv('tasks/result_1_verification.csv', index_col=False,delim_whitespace=True)
        pd.DataFrame(df.sum(), columns=['sum']).to_csv("tasks/result_4_1.csv")
        os.system('sshpass -p "tafraliang" scp -vr tasks/result_4_1.csv kalikho@172.16.117.17:/home/kalikho/icbc/verification_output/')
        print(datetime.datetime.now())
        print("Sent verification for Task 1")
        print("===")
        os.remove("tasks/result_1_verification.csv")
