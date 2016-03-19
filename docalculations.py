import uviswfc3etc
import acsetc
import numpy as np 
mass, logTe,logG,F336W,F555W = np.loadtxt("output286608781972.dat",usecols=[3,5,6,12,17],unpack=True)
F336W=F336W+13.23
mass=mass[F336W>17.7]
logG=logG[F336W>17.7]
logTe=logTe[F336W>17.7]
F555W=F555W[F336W>17.7]
F336W=F336W[F336W>17.7]

logR=-0.5*(logG-np.log10(27444)-np.log10(mass))
spectype=["O5V","O7V","O9V","B0V","B1V","B3V","B5V","B8V","A1V","A3V","A5V","F0V","F2V","F5V","F8V","G2V","G5V","G8V","K0V","K4V","K7V","M2V"]
temperature=[44500,38000,33000,30000,25400,18700,15400,11900,9230,8720,8200,7200,6890,6440,6200,5860,5770,5570,5250,4560,4060,3500]
Te=10**logTe
sptype=np.where(Te>temperature[0],spectype[1],spectype[0])
for i in range(1,len(spectype)-1):
    sptype=np.where(Te>temperature[i],sptype,spectype[i+1])

F475Xsnr=0*mass
F555Wsnr=0*mass
F814Wsnr=0*mass
CLEARsnr=0*mass
for i in range(len(F475Xsnr)):
    data=uviswfc3etc.constructdata('F475X','WFC3/UVIS/F336W',F336W[i],0.04,600)
    data["fbpgsfile"]=sptype[i]
    F475Xsnr[i]=uviswfc3etc.place_uviswfc3_request(data)
    data=acsetc.constructdata('F555W','CLEAR2S','WFC3/UVIS/F336W',F336W[i],0.04,600)
    data["fbpgsfile"]=sptype[i]
    F555Wsnr[i]=acsetc.place_acs_request(data)
    data["wfcfilt0"]="CLEAR1S"
    CLEARsnr[i]=acsetc.place_acs_request(data)
    data["wfcfilt1"]="F814W"
    F814Wsnr[i]=acsetc.place_acs_request(data)


print("#  1: mass    2 : Teff      3: F336W      4: F555W      5: logG       6: logR        7: F475Xsnr     8: F555Wsnr     9: F814Wsnr     10: CLEARsnr     11: spType"  )

for s in zip(mass,Te,F336W,F555W,logG,logR,F475Xsnr,F555Wsnr,F814Wsnr,CLEARsnr,sptype):
    print('%13.7e %13.7e %13.7e %13.7e %13.7e %13.7e %13.7e %13.7e %13.7e %13.7e %5s' % s)


if False:
    data=uviswfc3etc.constructdata('F475X','WFC3/UVIS/F336W',20,0.04,600)
    data["fbpgsfile"]="K4V"

    snr=uviswfc3etc.place_uviswfc3_request(data)
    print(snr)
