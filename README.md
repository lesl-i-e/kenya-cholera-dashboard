# Chapter 0 — Project Overview (Executive Summary)

## Project Title
**Spatio-Temporal Modeling of Climate-Driven Cholera Risk in Kenya**

## Overview
Cholera remains a recurrent public health threat in Kenya, with outbreaks exhibiting strong spatial and seasonal variability. Understanding how climatic factors interact with population distribution to influence cholera incidence is essential for early warning systems and targeted intervention planning.

This project develops a **district-level (Admin-2) spatio-temporal modeling framework** to quantify the relationship between cholera incidence and key climate variables across Kenya. Using surveillance data, high-resolution climate reanalysis products, population raster data, and administrative boundary shapefiles, the study integrates heterogeneous data sources into a unified analytical pipeline.

The final outputs of the project are:
- A clean, modeling-ready spatio-temporal dataset at **district–month resolution**
- A **Negative Binomial regression model** accounting for overdispersion and lagged climate effects
- An **interactive Streamlit dashboard** for visualizing cholera risk patterns across space and time

The project emphasizes **methodological rigor, transparent assumptions, and reproducibility**, prioritizing interpretability over black-box prediction.

---

## Key Objectives
- Quantify the association between cholera incidence and climate variability in Kenya  
- Identify dominant climatic drivers and temporal lag effects  
- Address spatial heterogeneity at the district level  
- Build an interpretable statistical baseline suitable for public health analysis  
- Deploy results through an interactive geospatial dashboard  

---

## Core Components

### Epidemiological Data
- District-level cholera surveillance records

### Climate Data
- ERA5 reanalysis products  
  - Temperature  
  - Precipitation  
  - Relative humidity  

### Population Data
- WorldPop gridded population estimates

### Spatial Data
- GADM administrative boundaries (Admin Level 2)

### Modeling Framework
- Negative Binomial regression with lagged covariates

### Visualization
- Streamlit-based interactive dashboard

---

## Final Deliverable
The project culminates in a **fully reproducible analytical pipeline** and an **interactive web application** that allows users to:
- Explore spatial patterns of cholera incidence  
- Inspect temporal trends and seasonality  
- Examine climate–cholera relationships across districts  
- Compare relative risk across Kenya  

> 📌 *Screenshot to be included in final version*  
> **Final Streamlit dashboard (map + time-series view)**

---

## Scope Note
This project is **analytical and exploratory**, not a real-time forecasting system. Results are intended to support understanding of climate–health relationships rather than operational outbreak prediction.

---

## Why This Matters
Climate-sensitive diseases such as cholera are expected to become more volatile under changing climate conditions. By combining **climate science, spatial analytics, and epidemiological modeling**, this project demonstrates how integrated data approaches can support evidence-based public health decision-making in resource-constrained settings.
