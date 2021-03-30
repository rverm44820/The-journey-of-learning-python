import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import time
import math
import datetime
import yfinance as yf
import winsound
now = time.time()
stock_list =   ['ABEV', 'ACND', 'ADMP', 'AEZS', 'AGEN', 'AGI', 'AHT', 'AIKI', 'AKBA', 'AMRN',
                'ARLO', 'ASM', 'ATNX', 'ATOS', 'AUY', 'AVGR', 'BBD', 'BOXL', 'BRFS', 'BRQS',
                'BTCS', 'BTG', 'CCO', 'CDEV', 'CEI', 'CFMS', 'CHS', 'CIDM', 'CIG',
                'CLVS', 'CPG', 'CRBP', 'CTXR', 'CVE', 'CX', 'DFFN', 'DGLY', 'DHY', 'DNN', 'DPW',
                'ECOR', 'EMAN', 'ESGC', 'EXK', 'EXPR', 'EXROF', 'FBIO', 'FTFT', 'GGB',
                'GNUS', 'GNW', 'GSAT', 'GTT', 'HEPA', 'HL', 'HMY', 'HTZGQ', 'HUGE', 'HVBTF',
                'IAG', 'IBIO', 'IDEX', 'IGC', 'INPX', 'INUV', 'ISR', 'ITRM', 'ITUB', 'IVR',
                'JAGX', 'JCS', 'KGC', 'KOS', 'KXIN', 'LKCO', 'LODE', 'LYG', 'MICT', 'MNKD',
                'MREO', 'MRIN', 'MUX', 'NAKD', 'NBRV', 'NEPT', 'NGD', 'NNVC', 'NOK', 'NOVN',
                'NXTD', 'OGI', 'OLB', 'ONTX', 'OPGN', 'OPK', 'PAVM', 'PHUN', 'POAI', 'POWW',
                'PTE', 'QTT', 'REI', 'RIG', 'RWLK', 'RYCEY', 'SAN', 'SENS', 'SESN', 'SHIP',
                'SIRI', 'SLGG', 'SNDL', 'SOLO', 'SOS', 'SSKN', 'SWN', 'TBLT', 'TELL', 'TNXP',
                'TRCH', 'TSNPD', 'TTOO', 'TXMD', 'TYME', 'UAMY', 'UEC', 'UGP', 'URG',
                'UUUU', 'VBIV', 'VISL', 'WATT', 'WWR', 'ZOM']
#.50-5.50  STOCKLIST
'''stock_list = [ 'ACAC', 'ACB', 'ACTG', 'ADT', 'AFMD', 'AGI', 'AGNC', 'ALTO',
              'ALUS', 'AM', 'AMC', 'AMCR', 'AMRN', 'AMRS', 'AMX', 'ANGI', 'APA', 'APHA', 'APRE',
              'APT', 'AQB', 'AQMS', 'AR', 'AUPH', 'AVXL', 'AYRO', 'BB', 'BCRX', 'BCS', 'BDN',
              'BNGO', 'BSBR', 'BTAQ', 'CAN', 'CBAT', 'CBB', 'CCJ', 'CCX', 'CDE', 'CLF',
              'CLNE', 'CLNN', 'CLOV', 'CLVR', 'CNHI', 'CNX', 'COTY', 'CPE', 'CRDF',
              'CRHC', 'CRMD', 'CRON', 'CVE', 'CX', 'CXW', 'CYDY', 'DB', 'DBC', 'DBI', 'DFEN',
               'DGNR', 'DOYU', 'DVAX', 'EBON', 'ENDP', 'ERIC', 'ERJ', 'ERX', 'ETRN', 'EVRI',
              'F', 'FAZ', 'FBP', 'FHN', 'FRO', 'FRSX', 'FSM', 'FSR', 'FTFT', 'FTI', 'FTOC',
              'FUSE', 'GBR', 'GE', 'GEO', 'GEVO', 'GFI', 'GILT', 'GLBS', 'GLUU', 'GOEV',
              'GOGO', 'GPK', 'GPRO', 'GT', 'HBAN', 'HBI', 'HEXO', 'HIMX', 'HL', 'HLIT', 'HMHC', 'HOL',
              'HPE', 'HST', 'INFN', 'ING', 'INO', 'IPOF', 'ISBC', 'ITUB', 'IZEA', 'JBLU', 'JDST',
              'JE', 'JUPW', 'KALA', 'KDMN', 'KERN', 'KGC', 'KIM', 'KMI', 'KMPH', 'KNDI', 'KODK',
              'KOPN', 'KPTI', 'KSMT', 'LABD', 'LC', 'LCY', 'LIZI', 'LKNCY', 'LOTZ', 'LU',
              'LUMN', 'LX', 'LXRX', 'M', 'MAC', 'MBRX', 'MBT', 'MGI', 'MIK', 'MITK', 'MOMO', 'MRO',
              'MTG', 'MUR', 'MVIS', 'NLY', 'NNDM', 'NOV', 'NRZ', 'NTN', 'NYCB', 'OEG', 'OPK', 'ORMP',
              'PAA', 'PAGP', 'PBCT', 'PBF', 'PBI', 'PBR', 'PCG', 'PDBC', 'PGEN', 'PGX',
              'PLNHF', 'POWW', 'PRCH', 'PSEC', 'PSLV', 'PSQ', 'PTEN', 'QRTEA', 'RRC', 'SABR', 'SBH',
              'SCO', 'SDC', 'SDOW', 'SDS', 'SID', 'SIRI', 'SKT', 'SLM', 'SLS', 'SM', 'SOLO', 'SOXS',
              'SP', 'SRNE', 'SRTY', 'STLA', 'TBA', 'TCS', 'TEVA','TGI', 'TRIT',
              'TWO', 'TZA', 'UA', 'UAVS', 'UMC', 'UNG', 'UVXY', 'UWMC', 'VCVC', 'VFF',
              'VG', 'VIAV', 'VIXY', 'VUZI', 'VYGVF', 'WIMI', 'WIT','WPF', 'WPRT', 'WWR',
              'XERS', 'YGMZ', 'YQ', 'ZNGA']'''
                

'''stock_list = ['dnn','ecor','exk','expr','geg','gnw','isr','nept','opk','qtt','rig','sskn','uec','swn','trch','nok','nxtd']'''

#stock_list = input('what stock would you like:  ').split()
#stock_list.append(f)
stocks = stock_list
count = 0
low_sma9 = 0
for i in range(500):#
    count+=1
    print('count',count)
    #data = yf.download(stocks ,period ='1d',interval='1m')
    for stock in stocks:
        #stock = input('what stock would you like:  ')
        
        data = yf.download(stock ,period ='2d',interval='1m')
        #print(data)
        
        for i in range(len(data)):
            volume=data['Volume'].rolling(window=1).mean()
            close =data['Close'].rolling(window=2).mean()
            high =data['High'].rolling(window=2).mean()
            low =data['Low'].rolling(window=2).mean()
            sma9 =data['Close'].rolling(window=9).mean()
            sma23 =data['Close'].rolling(window=23).mean()
            sma36 =data['Close'].rolling(window=36).mean()
            #vol_avg50=data['Volume'].rolling(window=50).mean()
            vol_avg25=data['Volume'].rolling(window=25).mean()
        time.sleep(1.5)    
        print(f'stock------- {stock} {close[-1]:.2f}')
        
        closediff1 = close[-1]-(close[-2])
        closediff2 = close[-1]-(close[-3])
        closediff3 = close[-1]-(close[-4])
        closediff4 = close[-1]-(close[-5])
        
        print(f'closediff1 {closediff1:.4f}')
        
        #if float(closediff1) > 0.06 or float(closediff2) > 0.06 or float(closediff3) > 0.06 or float(closediff4) > 0.06 :
            #winsound.Beep(1350, 100)
           # print(f'price surge {stock}')
        outz=sma9[-1]-sma9[-6]   
        if sma9[-1]>sma9[-6]:
            print(f'$ diff 5 min {outz:.4f}')
            if float(outz) >=.26:
                winsound.Beep(1250, 100)
                print(f'11111111111 {stock}')
                #write to a file 
               # file1 = open("stocklist.txt","a") 
               # ct = datetime.datetime.now() 
               # l =[f'{stock}  {close[-1]:.4f} {ct}\r\n']
               # file1.writelines(l)
                
                #file1.close()
        #time.sleep(.01)
        outa=sma9[-1]-sma9[-11]
        #if sma23[-1]>sma23[-11]:
        print(f'$ diff 10 min {outa:.4f}')
        #if sma23[-1]>sma23[-6]:
    
           # if float(outz) >=.02:
                
               # if sma23[-1]>sma23[-11]:

                 #   if outa >= .04:
                  #      print(f'2222222222222 {stock}')
                  #      winsound.Beep(1400,200)
            #winsound.Beep(400,200)
        #time.sleep(.01)
        outb=sma9[-1]-sma9[-21]
        #if sma23[-1]>sma23[-21]:
        print(f'$ diff 20 min {outb:.4f}')

        outc=sma9[-1]-sma9[-31]
        #if sma23[-1]>sma23[-31]:
        print(f'$ diff 30 min {outc:.4f}')

       # time.sleep(.01)
        outd=sma9[-1]-sma9[-41]
       # if sma23[-1]>sma23[-41]:
        print(f'$ diff 40 min {outd:.4f}')
        try:
           # time.sleep(.01)
            oute=sma9[-1]-sma9[-51]
           # if sma23[-1]>sma23[-51]:
            print(f'$ diff 50 min {oute:.4f}')
            
            #time.sleep(.01)
            outf=sma9[-1]-sma9[-61]
           # if sma23[-1]>sma23[-61]:
            print(f'$ diff 60 min {outf:.4f}')
        except:
            print('time error')
        #if sma23[-1] > sma23[-21]:  
           # if outz > .09:
           # winsound.Beep(1550, 200)
              #  print(f'3333333333333333 {stock}')
              #  winsound.Beep(1600, 200)
            #winsound.Beep(1750, 200)
        uptic0 = outf + oute + outd + outc + outb + outa
        if uptic0 > .45:
            winsound.Beep(550, 200)
            print(f'$ total --------- 60 min {uptic0:.4f}')
            file1 = open("stocklist.txt","a")
            ct = datetime.datetime.now() 
            l =[f'{stock}  {close[-1]:.2f} 60 min uptic {uptic0:.2f} {ct}\r\n']
            file1.writelines(l)
            file1.close()

            
        uptic1 =  outc + outb + outa
        if uptic1 > .15:
            winsound.Beep(950, 300)
            print(f'$ total --------- 30 min {uptic1:.4f}') 
            #write to a file 
            file1 = open("stocklist.txt","a") 
            ct = datetime.datetime.now() 
            l =[f'{stock}  {close[-1]:.2f} 30 min uptic {uptic1:.2f} {ct}\r\n']
            file1.writelines(l)
            file1.close()
        outt=sma9[-1]-sma9[-12]
        outu=sma9[-1]-sma9[-24]
        outv=sma9[-1]-sma9[-36]
                                            
        if  float(outz) > 0.01 :
            if  float(outa) > 0.02 :
                if  float(outb) > 0.04:
                    if float(outc) > 0.05:
                        winsound.Beep(550, 200)
                        print(f'444444444444444 {stock}')
                        #winsound.Beep(600, 100)
                        #winsound.Beep(650, 100)
                        winsound.Beep(1700, 100)
                        print(f'stock------- {stock}')
                        print(f'price {close[-1]:.4f} steady upward trend')
                        file2 = open("volandpriceinc.txt","a")
                        ct = datetime.datetime.now()
                        pv =[f' {stock}  {close[-1]:.4f} {ct}\r\n']
                        #out1 =[f'outt {outt:.2f} outu {outu:.2f} outv {outv:.2f} \r\n']
                        
                        file2.writelines(pv)
                        #file2.writelines(out1)
                    
        outl = sma23[-1]- sma23[-16]
        outk= 1/outl
        print(f'outk  {outk:.2f}')
        if outk > 10 and outk < 70:
            file3 = open("outk.txt","a")
            ct = datetime.datetime.now() 
            uv =[f' {stock}  {close[-1]:.4f} {ct}  {outk:.4f} \r\n']
            file3.writelines(uv)
        l=['']
        ct =['']
        
        
        #time.sleep(1.1)
