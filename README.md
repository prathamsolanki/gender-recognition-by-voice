# Gender Recognition by Voice and Speech Analysis

Dataset Source: [Kaggle Datasets: Gender Recognition by Voice](https://www.kaggle.com/primaryobjects/voicegender)

This dataset is released by [Kory Becker](https://github.com/primaryobjects) on [Kaggle](https://www.kaggle.com/) under [CC BY-NC-SA 4.0 License](https://creativecommons.org/licenses/by-nc-sa/4.0/).  

This database was created to identify a voice as male or female, based upon acoustic properties of the voice and speech. The dataset consists of 3,168 recorded voice samples, collected from male and female speakers. The voice samples are pre-processed by acoustic analysis in R using the seewave and tuneR packages, with an analyzed frequency range of 0hz-280hz (human vocal range).

# The Dataset

## The following acoustic properties of each voice are measured and included within the CSV:

* **meanfreq  :** mean frequency (in kHz)
* **sd	      :** standard deviation of frequency
* **median    :** median frequency (in kHz)
* **Q25       :** first quantile (in kHz)
* **Q75       :** third quantile (in kHz)
* **IQR       :** interquantile range (in kHz)
* **skew      :** skewness (see note in specprop description)
* **kurt      :** kurtosis (see note in specprop description)
* **sp.ent    :** spectral entropy
* **sfm       :** spectral flatness
* **mode      :** mode frequency
* **centroid  :** frequency centroid (see specprop)
* **peakf     :** peak frequency (frequency with highest energy)
* **meanfun   :** average of fundamental frequency measured across acoustic signal
* **minfun    :** minimum fundamental frequency measured across acoustic signal
* **maxfun    :** maximum fundamental frequency measured across acoustic signal
* **meandom   :** average of dominant frequency measured across acoustic signal
* **mindom    :** minimum of dominant frequency measured across acoustic signal
* **maxdom    :** maximum of dominant frequency measured across acoustic signal
* **dfrange   :** range of dominant frequency measured across acoustic signal
* **modindx   :** modulation index. Calculated as the accumulated absolute difference between adjacent measurements of fundamental frequencies divided by the frequency range
* **label     :** male or female
