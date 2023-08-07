#!/usr/bin/python3
import socket
import _thread
from array import array
from math import ceil
from struct import unpack
import numpy as np

#Hacking-Arena{top_s4c4t_p0wer_nah_nah_nah}

def TCP(conn, addr):
        buffer = array('B', [0] * 300)
        cnt = 0
        hexOf = lambda BUFFER: ','.join([hex(i) for i in BUFFER])
        while True:
                try:
                        conn.recv_into(buffer)
                        TID0 = buffer[0]   #Transaction ID      to sync
                        TID1 = buffer[1]   #Transaction ID 
                        ID = buffer[6]     #Unit ID
                        FC = buffer[7]     #Function Code
                        mADR = buffer[8]   #Address MSB
                        lADR = buffer[9]   #Address LSB
                        ADR = mADR * 256 + lADR 
                        LEN = 1
                        if FC not in [5,6]: 
                                LEN = buffer[10] * 256 + buffer[11]
                        BYT = LEN * 2
                        print("Received: ", hexOf(buffer[:6+buffer[5]]))
                        if (FC in [1, 2, 3, 4]):  # Read Inputs or Registers
                                DAT = array('B')
                                if FC < 3:
                                        BYT = ceil(LEN / 8)  # Round off the no. of bytes
                                        v = 85  # send 85,86.. for bytes.
                                        for i in range(BYT):
                                                DAT.append(v)
                                                v = (lambda x: x + 1 if (x < 255) else 85)(v)
                                        DATA = DAT
                                else:
                                        DAT = array('B', np.arange(cnt, LEN+cnt, dtype=np.dtype('>i2')).tobytes())
                                        DATA = [i for i in range(cnt, LEN+cnt)]
                                        print("LEN:")
                                        print(LEN) 
