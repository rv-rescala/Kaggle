from common import TRAIN_FILE

import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)

import seaborn as sns
import matplotlib.pyplot as plt

import tensorflow as tf

train_dataset = pd.read_csv(TRAIN_FILE)
train_dataset.shape

