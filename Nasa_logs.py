import pandas as pd
import numpy as np
import matplotlib as plt
import re
from collections import Counter

#====================================================================================================================== Q_01
# f=open('access_log_Aug95',"r")
# lines=f.readlines()
# hosts=[]
# for x in lines:
#     hosts.append(x.split(' - - ')[0])
# f.close()
#
# f2=open('access_log_Jul95','r', encoding= 'utf-8', errors='ignore')
# lines2=f2.readlines()
# hosts2=[]
# for y in lines2:
#     hosts2.append(y.split(' - - ')[0])
# f2.close()
#
# print ('Qtd de Hosts unicos: ', len(np.unique(hosts)), ' + ', len(np.unique(hosts2)), ' = ', len(np.unique(hosts)) + len(np.unique(hosts2)))
#====================================================================================================================== Q_02
#
# f=open('access_log_Aug95','r')
# lines=f.readlines()
#
# f2=open('access_log_Jul95','r', encoding= 'utf-8', errors='ignore')
# lines2=f2.readlines()
#
# counter = 0
# for x in lines:
#     if ' 404 ' in x:
#         counter = counter + 1
#         # print (x)
# print ('first: ',counter)
#
# for y in lines2:
#     if ' 404 ' in y:
#         counter = counter + 1
#         # print(y)
# print ('total: ',counter)

#
# f.close()
# f2.close()
#
# #df = pd.read_csv(lines,sep=" ", header=None, columns = ['Hosts', '-', '-', 'date', 'timezone', 'get', 'address', 'err', 'idk', 'idk2'])

# #====================================================================================================================== Q_03 e Q_04
#
# f=open('access_log_Aug95','r')
# lines=f.readlines()
#
# f2=open('access_log_Jul95','r', encoding= 'utf-8', errors='ignore')
# lines2=f2.readlines()
#
# host = []
# date = []
# address = []
# error = []
# bytes_amount = []
#
#
# for x in lines:
#     if ' 404 ' in x:
#         host.append([x.split(' ')[0]])
#         # dash1 = x.split(' ')[1]
#         # dash2 = x.split(' ')[2]
#         # y = x.split(' - - ')[1]
#         # temp = x.split(' ')[3], x.split(' ')[4]
#         # date.append([' '.join(temp)])
#
#         temp = x.split(' ')[3]
#         temp = temp.split(':')[0]
#         temp = temp.replace('[', '')
#         date.append([temp])
#
#         temp = x.split(' ')[5],x.split(' ')[6],x.split(' ')[7]
#         address.append([' '.join(temp)])
#
#         error.append([x.split(' ')[8]])
#
#         # bytes_amount.append([x.split(' ')[9]])
#
# for x in lines2:
#     if ' 404 ' in x:
#         host.append([x.split(' ')[0]])
#         # dash1 = x.split(' ')[1]
#         # dash2 = x.split(' ')[2]
#         # y = x.split(' - - ')[1]
#
#         # temp = x.split(' ')[3], x.split(' ')[4]
#         # date.append([' '.join(temp)])
#
#         temp = x.split(' ')[3]
#         temp = temp.split(':')[0]
#         temp = temp.replace('[','')
#         date.append([temp])
#         # print(temp)
#         temp = x.split(' ')[5], x.split(' ')[6], x.split(' ')[7]
#         address.append([' '.join(temp)])
#
#         error.append([x.split(' ')[8]])
#
#         # bytes_amount.append([x.split(' ')[9]])
#
#         # print (bytes_amount)
# # df_404 = pd.DataFrame(
# #     { 'Host': host,
# #       'date': date,
# #       'address': address,
# #       'error': error
# #     })
#
# df_404 = pd.DataFrame(np.column_stack([host, date, address, error]),
#                       columns=['host','date','address','error'])
#
#
#
# print (df_404)
# # print (df_404['host'].value_counts())
# # print (df_404['date'].value_counts())
#
# f.close()
# f2.close()

#====================================================================================================================== Q_05

f=open('access_log_Aug95','r')
lines=f.readlines()

f2=open('access_log_Jul95','r', encoding= 'utf-8', errors='ignore')
lines2=f2.readlines()

host = []
date = []
address = []
error = []

soma_byte = 0
temp = 0
for x in lines:

    if '\n' in x.split(' ')[-1]:
        temp = x.split(' ')[-1].replace('\n', '0')
    if '-' in x.split(' ')[-1]:
        temp = x.split(' ')[-1].replace('-', '0')
    soma_byte = soma_byte + int(temp)
print(soma_byte)

for x in lines2:

    if '\n' in x.split(' ')[-1]:
        temp = x.split(' ')[-1].replace('\n', '0')

    if '-' in x.split(' ')[-1]:
        temp = x.split(' ')[-1].replace('-', '0')

    soma_byte = soma_byte + int(temp)


print(soma_byte)
f.close()
f2.close()