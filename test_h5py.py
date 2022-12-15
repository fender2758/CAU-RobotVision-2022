import numpy as np
import h5py
f_train= h5py.File('audioset_hdf5s/mp3/FSD50K.train_mp3.hdf','r')
targets = np.array(f_train['target'])
uniques, counts = np.unique(targets,
          return_counts = True)
for u, c in zip(uniques, counts):
    print(u, c)
print(len(counts))