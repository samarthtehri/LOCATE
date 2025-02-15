# -*- coding: utf-8 -*-
"""597FinalProject.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1p7QKHWZDnwxSsHSqVnOObPdgn56RhEir
"""

# Get gdown to download large google files. Manually insert best_seen.pth and best_unseen.pth here
!pip install gdown
#!gdown 1OEz25-u1uqKfeuyCqy7hmiOv7lIWfigk # sometimes it says it cannot retrieve, alternate link below. Please uncomment it
!gdown 1eFpg24xWTAHSWX3eRojFETA8SEA31lnd

# Unzip large google file quietly and remove zip file
!unzip -q AGD20K.zip
!rm AGD20K.zip

# Commented out IPython magic to ensure Python compatibility.
# Clone and check repository - sanity check
!git clone https://github.com/Reagan1311/LOCATE.git
# %cd LOCATE/
# %ls

# Install Dependencies and other requirements by the LOCATE project
!pip install torch==1.12.1+cu116 torchvision==0.13.1+cu116 torchaudio==0.12.1 --extra-index-url https://download.pytorch.org/whl/cu116
!pip install -r requirements.txt

# Check current GPU config before running train and test
!nvidia-smi

# Commented out IPython magic to ensure Python compatibility.
# Now for the seen part. Due to time constraints, limiting epochs to 5
# Run Training as per the LOCATE repository but Modified Train code for slightly faster code
# modified num_workers (inc test) to 2 for colab efficiency, show every 50 steps
# modified batch size to 32 and epochs to 5 to utilize gpu memory, testing on large batch size and less epochs
# NOTE: done on V100 GPU on colab, each 100 step update takes about 5 mins to show. For faster sense of updates, try step size of 10
# improved code calculation, reduced some loops using parallelization
# %cd LOCATE/
!python trainMOD.py --data_root ../AGD20K/ --batch_size 32 --num_workers 2 --test_num_workers 2 --epochs 5

# Run Testing as per the LOCATE repository with best paths seen
!python test.py --data_root ../AGD20K/ --model_file ../best_seen.pth

# Run Testing - from the modified training ones. (trainMod)(manually enter from save_models/) (seen)
!python test.py --data_root ../AGD20K/ --model_file save_models/20231211_221135/best_model_5_1.259_0.394_1.142.pth

# Commented out IPython magic to ensure Python compatibility.
# Now for the unseen part. Due to time constraints, limiting epochs to 5
# Run Training as per the LOCATE repository but Modified Train code for slightly faster code
# modified num_workers (inc test) to 2 for colab efficiency, show every 50 steps
# modified batch size to 32 and epochs to 5 to utilize gpu memory, testing on large batch size and less epochs
# NOTE: done on V100 GPU on colab, each 100 step update takes about 5 mins to show. For faster sense of updates, try step size of 10
# improved code calculation, reduced some loops using parallelization
# %cd LOCATE/
!python trainMOD.py --data_root ../AGD20K/ --batch_size 32 --num_workers 2 --test_num_workers 2 --epochs 5 --divide Unseen

# Run Testing as per the LOCATE repository with best paths unseen (don't forget --divide Unseen)
!python test.py --data_root ../AGD20K/ --model_file ../best_unseen.pth --divide Unseen

# Run Testing - from the modified training ones. (trainMod)(manually enter from save_models/) (unseen) (don't forget --divide Unseen)
!python test.py --data_root ../AGD20K/ --model_file save_models/20231212_010025/best_model_5_1.473_0.353_1.109.pth --divide Unseen