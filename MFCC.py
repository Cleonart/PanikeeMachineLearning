# Import Dependencies
import librosa
import matplotlib.pyplot as plt
import python_speech_features
import numpy as np

class MFCC():
    """MFCC shorther hand function"""
    sampleRate = 8000
    numMFCC    = 16

    def calcMFCC(self,path=None):
        """ Calculate MFCC from given path """

        if path == None or path == "":
            raise Exception("ERROR!: Please specify a path")
            return

        # Load Wavefile
        signal, fs = librosa.load(path, sr = self.sampleRate)

        # Create MFCCs from sound clip
        mfccs = python_speech_features.base.mfcc(signal,
                                                 samplerate=fs,
                                                 winlen=0.256,
                                                 winstep=0.050,
                                                 numcep=self.numMFCC,
                                                 nfilt = 26,
                                                 nfft  = 2048,
                                                 preemph=0.0,
                                                 ceplifter=0,
                                                 appendEnergy=False,
                                                 winfunc=np.hanning)
        return mfccs.transpose()

    def extractFeatures(self, path=None):
        """ Extract the feature from audio file """

        # If path is None return error
        if path == None:
            raise Exception("ERROR! Path can't be None: Specify the path")
            return

        # Create the mfccs for the path
        mfccs = self.calcMFCC(path)
        return mfccs

