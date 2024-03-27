import os, sys

import streamlit as st
import matplotlib.pyplot as plt
import numpy as np

os.system("pip install -r requirements.txt")

rand=np.random.normal(1,2,size=20)
fig,ax = plt.subplots()
ax.hist(rand, bins=15)
st.pyplot(fig)