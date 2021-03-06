import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl
import math
import os
from os import path
import platform

path = os.getcwd()

if platform.system() == "Windows":
    path = path.replace('results\graficos' , '')
else :
    path = path.replace('results/graficos' , '')

plt.rc('text', usetex=True)
if platform.system() == "Windows":
    plt.rc('font',**{'family':'DejaVu Sans','serif':['Times']})
else :
    plt.rc('font',**{'family':'serif','serif':['Times']})


# plt.rc('font',**{'family':'serif'})
# plt.rc('text', usetex=True)


#########################
##    controles        ##
#########################

plt.rcParams.update({'font.size': 32})


Ret = " 150"          #oq ta no images
dnss = "150_071"     #oq ta no DNS
Pr = "_0.71"            #oq ta no images, para velocidade, ""
e = np.zeros(400)
metodo = "classico"                 # Segundo oq ta no image

tamanho = 10
aspectratio = 0.5


######################### vetor espaço...

for i in range(1 , 400):
    e[i] = (i - 0.5) * (1/(400 - 0.5) * int(Ret))



######################## Gráfico do Prandtl...

# plt.figure(figsize=(tamanho , tamanho * aspectratio))

# prandtl = np.loadtxt(path + "DNS/Prt_RE_640_071.txt", dtype='float')
# spaco = prandtl[: , 1]
# prt = prandtl[: , 5]

# plt.plot(spaco / 640 ,prt , color='black' , linestyle=":" , label=r"$Re_\tau = 640$ , $Pr = 0.71$")

# prandtl = np.loadtxt(path + "DNS/Prt_RE_640_0025.txt", dtype='float' )
# spaco = prandtl[: , 1]
# prt = prandtl[: , 5]

# plt.plot(spaco /640,prt , color='black', linestyle="--" , label=r"$Re_\tau = 640$ , $Pr = 0.025$")

# prandtl = np.loadtxt(path + "DNS/Prt_RE_395_071.txt", dtype='float')
# spaco = prandtl[: , 1]
# prt = prandtl[: , 5]

# plt.plot(spaco /395,prt, color='black', linestyle="-" , label=r"$Re_\tau = 395$ , $Pr = 0.71$")

# prandtl = np.loadtxt(path + "DNS/Prt_RE_395_0025.txt", dtype='float' )
# spaco = prandtl[: , 1]
# prt = prandtl[: , 5]

# plt.plot(spaco /395,prt, color='black', linestyle="-.", label=r"$Re_\tau = 395$ , $Pr = 0.025$")


# plt.xlabel(r'  $ {\tilde{y}}/{Re_\tau} $ ',fontsize=20)
# plt.ylabel(r'$ Pr_t $',fontsize=20)
# plt.subplots_adjust(top=0.9 , bottom=0.19)
# plt.xlim(0,1)
# plt.legend(fontsize=21 , frameon=False)
# plt.ticklabel_format(style='sci', axis='x', scilimits=(0,0) , fontsize= 10)
# plt.ticklabel_format(style='sci', axis='y', scilimits=(0,0) , fontsize= 10)
# plt.savefig('images/DNS_PRt.png')
# plt.show(block=False)




####################### Gráficos gerais das temperaturas...
tamanho = 10
aspectratio = 0.4



plt.figure(figsize=(tamanho , tamanho * aspectratio))

dados = np.loadtxt("image" + Ret + "." + Pr  + "_400_" + metodo + ".txt", dtype='float')

if platform.system() == "Windows":
    dns = np.loadtxt(path + "\DNS\DNS_RE_"+dnss + ".txt", dtype='float')
else :
    dns = np.loadtxt(path + "DNS/DNS_RE_"+dnss + ".txt", dtype='float')




plt.plot(e , dados , color='black' , linestyle='-', label= r'Present Work')
#plt.plot(- e , dados , color='black', linestyle='-')

plt.plot(int(Ret) - dns[:, 1] , dns[:, 2] , color='black' , linestyle='-.', label= r'DNS')
#plt.plot(dns[:, 1]- int(Ret) , dns[:, 2] , color='black' , linestyle='-.')

plt.xlim(0 , int(Ret))
plt.ylim(0 , max([max(dados) , max(dns[:, 2])]) * 1.2)
plt.legend(fontsize=35 , frameon=False)
ax = plt.gca()

label = ax.set_xlabel(r' \textbf{ $ \tilde{y} $ }',fontsize=35)
ax.xaxis.set_label_coords(0.84, -0.025)

label = ax.set_ylabel(r'\textbf{$ \tilde{\overline{T^\ast}} $}',fontsize=38)
ax.yaxis.set_label_coords(-0.03, 0.70)

if platform.system() == "Windows":
    plt.savefig('images\Temperature_' + dnss + '_' + metodo + '.png' , bbox_inches='tight')
else:
    plt.savefig('images/Temperature_' + dnss + '_' + metodo + '.png' , bbox_inches='tight')

plt.subplots_adjust(top=0.9 , bottom=0.15)
plt.show()




####################### Gráficos do algorítmo genético...
# tamanho = 10
# aspectratio = 0.5


# plt.figure(figsize=(tamanho , tamanho * aspectratio))

# gene = np.loadtxt(path + "results/Gene395_0025_400_Cefisico.txt", dtype='float')

# plt.plot(gene[:,0] / 1.87, gene[:,2] , 'bs', color='black', label= r'Simulated')
# plt.xlabel(r'  $ Pr_t $ ',fontsize=31)
# plt.ylabel(r'L2 norm',fontsize=31)
# plt.subplots_adjust(top=0.9 , bottom=0.19)
# plt.savefig('images/Genetic_amostra.png')
# plt.show()









