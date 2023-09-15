import altair as alt
import numpy as np
import pandas as pd
import streamlit as st
from vega_datasets import data

st.header('st.write')

# Example 1
st.write('Hello, *World!* 😎')

# Example 2
st.write(1234)

# Example 3 ie printing out dataframes

df = pd.DataFrame({
    'Names': ['A', 'B', 'C'],
    'Age': [12, 56, 34]
})

st.write(df)

# Example 5 - string interpolation
st.write('This is a sample dataframe:', df, 'see how it looks!')

# Example 6 - Drawing charts

df2 = pd.DataFrame(
    np.random.randn(200, 3),
    columns=['a', 'b', 'c']
)

st.write(df2)

c = alt.Chart(df2).mark_circle().encode(
    x='a', y='b', size='c', tooltip=['a', 'b', 'c']
)

st.write(c)

# Example with other Vega datasets
st.write(data.list_datasets())
iris = data.iris()
st.write(iris.columns)

st.write('Plotting the Iris dataset')
iris_chart = alt.Chart(data=iris).mark_circle(size=65).encode(
    x="petalLength",
    y="petalWidth",
    color="species",
    tooltip=["petalLength", "petalWidth"]
)

st.write(iris_chart)

# Plotting the airports dataset
airports = data.airports()

# Read in the polygons
states = alt.topo_feature(data.us_10m.url, feature='states')
input_dropdown = alt.binding_select(options=[
    "albers",
    "albersUsa",
    "azimuthalEqualArea",
    "azimuthalEquidistant",
    "conicEqualArea",
    "conicEquidistant",
    "equalEarth",
    "equirectangular",
    "gnomonic",
    "mercator",
    "naturalEarth1",
    "orthographic",
    "stereographic",
    "transverseMercator"
], name='Projection ')
param_projection = alt.param(value="equalEarth", bind=input_dropdown)

# US states background
background = alt.Chart(states).mark_geoshape(
    fill="lightgray",
    stroke='white'
).properties(
    width=500,
    height=300
).project('albersUsa')

# airport positions on background
points = alt.Chart(airports).mark_circle(
    size=10,
    color='steelblue'
).encode(
    longitude='longitude:Q',
    latitude='latitude:Q',
    tooltip=['name', 'city', 'state']
)

st.write(background + points)
