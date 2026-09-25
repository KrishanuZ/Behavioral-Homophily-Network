import numpy as np
import pickle
import streamlit as st
import matplotlib.pyplot as plt
import networkx as nx

st.title("Behavorial Homophily Network")
st.markdown("###Network")

threshold = st.slider("Similarity Threshold", min_value=0.8, max_value=0.99)
metric = st.selectbox("Choose Metric", ["Degree", "Betweenness", "Clustering Coefficient"])

st.pyplot()