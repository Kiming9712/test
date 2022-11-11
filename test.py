import numpy as np #调用库
import pandas as pd
import openpyxl
import pymrio

# exio3 = pymrio.parse_exiobase3(path='D:/训练/IOT_1997_ixi.zip')
# exio3.calc_all()#补充缺失值
# z = exio3.Z
# y = exio3.Y
# Z = np.array(z)
# Y = np.array(y)
# # Z = np.where(Z>0,Z,0)
# # Y = np.where(Y>0,Y,0) #7987*343
# print(y)
# # y_1 = np.loadtxt(r'D:\训练\IOT_1997_ixi\IOT_1997_ixi\Y.txt',dtype=None)
# # print(y_1)

z = pd.read_excel('D:/训练/2017i_e.xlsx',sheet_name=0,header=0,index_col=0)

Z = np.array(z)
Z = np.where(Z>0,Z,0)
y = pd.read_excel('D:/训练/2017i_e.xlsx',sheet_name=1,header=0,index_col=[0,1])
Y = np.array(y)
Y = np.where(Y>0,Y,0)
print(Z.shape)
print(Y.shape)
f = pd.read_excel('D:/训练/F.xlsx',sheet_name=1,header=0,index_col=0)
print(f)
F = np.array(f)

#参数处理
y1 = np.zeros([990,30])#合并国家内部产出总值，共30个国家
print(y1.shape)
for i in range(30):
   y1[:,i]= np.sum(Y[:,5*i:5+5*i],axis=1)
print(y1)
fd = np.zeros([990,990])
for i in range(30):
    for j in range(30):
        fd[33*i:33+33*i,33*j:33+33*j]=np.diag(y1[33*i:33+33*i,j].flatten())
# t_fd = np.sum(np.sum(fd,axis=1))
# t_y1 = np.sum(np.sum(y1,axis=1))
# print(t_fd)
# print(t_y1) #检验
x = np.sum(Z,axis=1)+np.sum(fd,axis=1)
x[x==0] = 0.00001
x = x.reshape(990,1)
dd = F/x
d = np.diag(dd.flatten())
A = Z/x.T
L = np.linalg.inv(np.eye(990)-A)
# 环境足迹计算
c = np.matmul(d,L)
wf = np.matmul(c,fd)
dwu = np.sum(wf,axis=1)
vwu = np.sum(wf,axis=0) #足迹列求和

# 结果处理与分析
#消费者水足迹
WFC = np.zeros([30,990])
for i in range(30):
    for j in range(30):
        WFC[i,33*j:33+33*j]=np.sum(wf[33*i:+33+33*i,33*j:33+33*j],axis=0)
#生产者水足迹
WFP = np.zeros([30,990])
for i in range(30):
    for j in range(30):
        WFP[j,33*i:33+33*i]=np.sum(wf[33*i:+33+33*i,33*j:33+33*j],axis=0)

co_1 = pd.read_excel(r'D:/训练/F.xlsx',sheet_name=2,usecols=[0])#990个地区名称，usecols表示选取第几列内容
co_2 = pd.read_excel(r'D:/训练/F.xlsx',sheet_name=2,usecols=[1])#990个部门名称
co_3 = pd.read_excel(r'D:/训练/F.xlsx',sheet_name=2,usecols=[2])#30个国家名称
# print(co_1)
# print(co_2)
wfc = pd.DataFrame(WFC,columns=[co_1['region'],co_2['sector']])
wfc['region'] = co_3
wfc = wfc.set_index(['region'],drop=True)
print(wfc)
# wfc['region'] = co_3['region_1']
# wfc = wfc.set_index(['region_1'],drop=True)
# wfc.to_excel('D:/训练/2017_WFC.xlsx',sheet_name='2017_wfc')#存贮计算的足迹数据原表

WFC_c_sec = np.zeros([30,30])
for i in range(30):
    WFC_c_sec[:,i] = np.sum(WFC[:,33*i:33+33*i],axis=1)
print(WFC_c_sec)
WFC_c_sec = pd.DataFrame(WFC_c_sec)
WFC_c_sec.to_excel('D:/训练/2017_WFC_c.xlsx',sheet_name='2017_wfc')#存贮计算的足迹数据原表
# 项目合并
# stata_1 = np.zeros([30,150])
# for i in range(30):
#     stata_1[i,:] = y.iloc[23+i*42] + y.iloc[31 + i * 42] + y.iloc[32 + i * 42] + y.iloc[33 + i * 42] + y.iloc[34 + i * 42] + y.iloc[35 35+ i * 42] + y.iloc[36 + i * 42] + y.iloc[37 + i * 42] + y.iloc[38 + i * 42] + y.iloc[41 + i * 42]
# stata_2 = np.zeros([30,1260])
# for i in range(30):
#     stata_2[i,:] = z.iloc[23+i*42] + z.iloc[31 + i * 42] + z.iloc[32 + i * 42] + z.iloc[33 + i * 42] + z.iloc[34 + i * 42] + z.iloc[35 + i * 42] + z.iloc[36 + i * 42] + z.iloc[37 + i * 42] + z.iloc[38 + i * 42] + z.iloc[41 + i * 42]
# print(stata_2)
# stata_3 = np.zeros([990,30])
# for i in range(30):
#     stata_3[:,i] = z.iloc[:,23+i*42] + z.iloc[:,31 + i * 42] + z.iloc[:,32 + i * 42] + z.iloc[:,33 + i * 42] + z.iloc[:,34 + i * 42] + z.iloc[:,35 + i * 42] + z.iloc[:,36 + i * 42] + z.iloc[:,37 + i * 42] + z.iloc[:,38 + i * 42] + z.iloc[:,41 + i * 42]
# print(stata_3)
# stata_3 = pd.DataFrame(stata_3)
# stata_3.to_excel('D:/训练/qita.xlsx',sheet_name='1997_wfc')#存贮计算的足迹数据原表






