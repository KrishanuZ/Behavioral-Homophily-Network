import numpy as np
import pickle
import streamlit as st
import matplotlib.pyplot as plt
import networkx as nx

st.title("Behavorial Homophily Network")
st.markdown("###Network")

threshold = st.sidebar.slider("Similarity Threshold", min_value=0.8, max_value=0.99)

st.pyplot()