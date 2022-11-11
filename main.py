# 数据读取
# 参数处理
# 环境足迹计算
# 结果处理与分析


import numpy as np #调用库
import pandas as pd
import openpyxl
import pymrio
# 数据读取
exio3 = pymrio.parse_exiobase3(path='D:/训练/IOT_1997_ixi.zip')
exio3.calc_all()#补充缺失值
z = exio3.Z
y = exio3.Y
Z = np.array(z)
Y = np.array(y)
Z = np.where(Z>0,Z,0)
Y = np.where(Y>0,Y,0) #7987*343
print(Y.shape) #查看Y是否符合7988*343行列式矩阵
f = exio3.satellite.F
f1 = f.loc[f.index.str.startswith('Water Consumption Blue',na=False)]
f1_sum = f1.sum(axis=0).to_frame()#axis = 0时为每一列的求和，= 1 时为每一行的求和
F = np.array(f1_sum)
print(F.shape)
# 参数处理
y1 = np.zeros([7987,49])#合并国家内部产出总值，共49个国家
print(y1.shape)
for i in range(49):
   y1[:,i]= np.sum(Y[:,7*i:7+7*i],axis=1)
print(y1)
fd = np.zeros([7987,7987])
for i in range(49):
    for j in range(49):
        fd[163*i:163+163*i,163*j:163+163*j]=np.diag(y1[163*i:163+163*i,j].flatten())
# print(fd.shape)
# t_fd = np.sum(np.sum(fd,axis=1))
# t_y1 = np.sum(np.sum(y1,axis=1))
# print(t_fd)
# print(t_y1) #检验
x = np.sum(Z,axis=1)+np.sum(fd,axis=1)
x[x==0] = 0.00001
x = x.reshape(7987,1)
dd = F/x
d = np.diag(dd.flatten())
A = Z/x.T
L = np.linalg.inv(np.eye(7987)-A)
# 环境足迹计算
c = np.matmul(d,L)
wf = np.matmul(c,fd)
dwu = np.sum(wf,axis=1)
vwu = np.sum(wf,axis=0) #足迹列求和
print(dwu)
# 结果处理与分析
#消费者水足迹
WFC = np.zeros([49,7987])
for i in range(49):
    for j in range(49):
        WFC[i,163*j:163+163*j]=np.sum(wf[163*i:+163+163*i,163*j:163+163*j],axis=0)
#生产者水足迹
WFP = np.zeros([49,7987])
for i in range(49):
    for j in range(49):
        WFP[j,163*i:163+163*i]=np.sum(wf[163*i:+163+163*i,163*j:163+163*j],axis=0)
WFC_c_sec = np.zeros([49,163])
for i in range(49):
    WFC_c_sec[i,0:163] = np.sum(WFC[0:49,163*i:163+163*i],axis=0)
WFP_c_sec = np.zeros([49,163])
for i in range(49):
    WFP_c_sec[i,0:163] = np.sum(WFP[0:49,163*i:163+163*i],axis=0)
#内部水足迹
IWF = np.zeros([49,163])
for i in range(49):
    IWF[i,0:163] = WFC[i,163*i:163+163*i]
#虚拟水进口
VWI = np.zeros([49,163])
VWI = WFC_c_sec - IWF
#虚拟水出口
VWE = np.zeros([49,163])
VWE = WFP_c_sec - IWF
WFC = pd.DataFrame(WFC)
WFC.to_excel('D:/训练/1997_WFC.xlsx',sheet_name='1997_wfc')#存贮计算的足迹数据原表
#添加表头
# co_1 = pd.read_excel(r'文件路径',sheet_name=2,usecols=[0])#7987个地区名称，usecols表示选取第几列内容
# co_2 = pd.read_excel(r'文件路径',sheet_name=2,usecols=[1])#7987个部门名称
# co_3 = pd.read_excel(r'文件路径',sheet_name=2,usecols=[2])#49个国家名称
# wfc = pd.DataFrame(WFC,colums=[co_1['region'],co_2['sector']])
# wfc['region'] = co_3['region']
# wfc = wfc.set_index(['region'],drop=True)
# wfc = wfc.div(1000) #单位换算






