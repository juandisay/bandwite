#!/usr/bin/env python
__author__= 'juandisay'

import time,sys,os

def headerkomandanbiarkekinian():
   if os.name == 'posix':
      os.system('clear')
   else:
      pass#nger 
   print '''
          Cek Bandwidthnya dulu ,Lets go...
        '''
class networks:
    cc_rx = []
    cc_tx = []
    def __init__(self,interface):
        try:
            self.rx_data,self.tx_data = self.ncup_cucuna(interface)
            self.cc_rx.append(self.rx_data)
            self.cc_tx.append(self.tx_data)
            self.update()
        except TypeError :
            time.sleep(1)
            print
            print '''               
                  [!] interface gak dikenali,coba cek interface yang tersedia!
                  '''
    def ncup_cucuna(self,interface):
        for line in open('/proc/net/dev', 'r'):
            if interface in line:
                data = line.split('%s:' % interface)[1].split()
                rx_data, tx_data = (data[0], data[8])
                return (rx_data, tx_data)

    def update(self):
        
        if len(self.cc_rx) == len(self.cc_tx) and len(self.cc_rx) and len(self.cc_rx) > 1:
            self.update_tx = (int(self.cc_tx[-1])/1000)-(int(self.cc_tx[-2])/1000)
            self.update_rx = (int(self.cc_rx[-1])/1000)-(int(self.cc_rx[-2])/1000)
            print ('''
   Bandwidth Monitor
   #################
   Up  : %s KB/s      
   Down: %s KB/s      
   #################         ''') % (self.update_tx,self.update_rx)
def input_interface():
    data = sys.argv
    return data[1]

if __name__ == '__main__':
    headerkomandanbiarkekinian()
    
    while True:
        os.system('which app')
        networks(input_interface())
        time.sleep(1)
        os.system('clear')
        
#special thanks to Dream theater,Kim Kardashian, ayu tingting, sarah azhari, Duo srigala.LOL
#license under stocking Kim Kardashian
