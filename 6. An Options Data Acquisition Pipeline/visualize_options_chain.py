import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.cm as cm
from mpl_toolkits.mplot3d.axes3d import Axes3D
from mpl_toolkits.mplot3d import proj3d
from datetime import datetime
### 0. Function

def filter_viz(df):
    df_show = df[(df.strikePrice >= strike_user[0]) & 
        (df.strikePrice <= strike_user[1]) &
        (df.expirationDate >= expiry_user[0]) &
        (df.expirationDate <= expiry_user[1]) &
        (df.mark >= 0) &
        (df.mark <= price_user)]
    return df_show

### 0. Load data

import os
path = os.path.dirname(__file__)
my_file = path+'/data/df_all.csv'
df = pd.read_csv(my_file).iloc[:,1:]
df_0 = pd.read_csv(path+'/data/df_0900.csv').iloc[:,1:] # Set first quote of day as baseline

# slider boundaries:
lowerStrike, upperStrike = np.min(df['strikePrice']), np.max(df['strikePrice'])
lowerExpiry, upperExpiry = 1639774800000, 1670000000000
lowerPrice, upperPrice = 0, 200

### 2.1 User inputs time of day

st.title("Today's NVDA Option Chains")
st.write("Price movements on option chains for NVIDIA Corporation (NVDA).")
st.write("Slide the slider to see how prices changed over the example trading day.")

# Slider: Need time of day for heatmap
timeofday  = st.slider('Time of Day',  min_value=900, max_value=1600, step=100)
if timeofday != 900:
    csv_file = path+'/data/df_'+str(timeofday)+'.csv'
    df = pd.read_csv(csv_file).iloc[:,1:]
st.write(f"Quotes shown obtained at {('0'+str(timeofday))[-4:]}, Thu Dec 16th, 2022")

### 2.2 user inputs strike, expiry, price parameters
st.write("Choose your parameters of interest:")
strike_user = st.slider('Strike prices (min, max)',
                        min_value=int(lowerStrike),
                        max_value=int(upperStrike),
                        value=(250,350))

expiry_user = st.slider('Expiry dates range (min, max)', 
                        min_value=int(lowerExpiry),
                        max_value=int(upperExpiry),
                        value=(1639774800000,1660000000000),
                       step=10000000)

price_user = st.slider('Max premium',
                      min_value=int(lowerPrice),
                      max_value=int(upperPrice),
                      value=30)


# Prepare baseline graph
df_0 = filter_viz(df_0)

df_0c = df_0[(df_0.putCall == 'CALL')]
x0c = df_0c['strikePrice']
y0c = df_0c['expirationDate']
z0c = df_0c['mark']

df_0p = df_0[(df_0.putCall == 'PUT')]
x0p = df_0p['strikePrice']
y0p = df_0p['expirationDate']
z0p = df_0p['mark']

# Prepare other graphs
df_show = filter_viz(df)

# 1. Prepare figure & boundaries
fig = plt.figure(figsize=(16,16))
ax = fig.add_subplot(projection='3d')
ax.set_xlabel('Strike Price ($)')
ax.set_ylabel('Expiration Date (epoch)')
ax.set_zlabel('Option Price ($)')

ax.set_xlim(left=strike_user[0], right=strike_user[1])
ax.set_ylim(bottom=expiry_user[0], top=expiry_user[1])
ax.set_zlim(bottom=0, top=price_user)

# 2. Plot call options with up-arrow marker
df_c = df_show[(df_show.putCall == 'CALL')]
x = df_c['strikePrice']
y = df_c['expirationDate']
z = df_c['mark']
marker = '^'

if timeofday != 900:
    hue = df_c['pctChange']
    ax.scatter(x, y, z, c=hue.map(cm.PuOr), marker=marker)
else:
    ax.scatter(x0c, y0c, z0c, c='k', marker=marker)

# 3. Plot put options with down-arrow marker
df_p = df_show[(df_show.putCall == 'PUT')]
x = df_p['strikePrice']
y = df_p['expirationDate']
z = df_p['mark']
marker = 'v'

if timeofday != 900:
    hue = df_p['pctChange']
    ax.scatter(x, y, z, c=hue.map(cm.PuOr), marker=marker)
else:
    ax.scatter(x0p, y0p, z0p, c='k', marker=marker)

# 5. Final adjustments
ax.set_box_aspect((1, 3, 1.5))
ax.view_init(10, -75)

st.pyplot(fig)

