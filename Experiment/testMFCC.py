import os, sys
currentdir = os.path.dirname(os.path.realpath(__file__))
parentdir = os.path.dirname(currentdir)
sys.path.append(parentdir)

from MFCC import MFCC

mfcc = MFCC()
mfcc_ = mfcc.calcMFCC("../Testdata/noise/1.wav")
print(mfcc_.shape)
