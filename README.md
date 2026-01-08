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

# Chapter 1 — Background and Motivation

## 1.1 Cholera as a Public Health Challenge
Cholera remains a significant public health concern in many low- and middle-income countries, particularly in regions with limited access to clean water, adequate sanitation, and robust healthcare infrastructure. The disease is characterized by acute watery diarrhea and can rapidly lead to severe dehydration and death if not treated promptly. Despite being both preventable and treatable, cholera continues to cause recurrent outbreaks across Sub-Saharan Africa.

Kenya has experienced repeated cholera outbreaks over the past decades, often linked to seasonal climatic variability, population mobility, and infrastructural vulnerabilities. These outbreaks place a substantial burden on public health systems and disproportionately affect vulnerable and underserved populations.

---

## 1.2 Climate–Disease Interactions
A growing body of empirical evidence demonstrates that climatic factors play a critical role in the transmission dynamics of cholera. Key variables such as temperature, precipitation, and humidity influence:
- The survival and proliferation of *Vibrio cholerae* in aquatic environments  
- Water contamination pathways and environmental reservoirs  
- Human exposure patterns and water-use behavior  

In East Africa, seasonal rainfall and temperature variability have been repeatedly associated with fluctuations in cholera incidence. However, the strength, direction, and timing of these relationships vary across spatial and temporal scales. Capturing these interactions at finer administrative levels is therefore essential for localized risk assessment and the development of effective early warning systems.

---

## 1.3 Motivation for a District-Level Modeling Approach
Many existing cholera studies in the region operate at national or provincial scales, which can obscure important local heterogeneity in disease risk. Kenya’s administrative districts (Admin-2 level) represent a meaningful analytical unit for:
- Public health planning and intervention design  
- Resource allocation and prioritization  
- Surveillance, monitoring, and response coordination  

By modeling cholera incidence at the district level, this study aims to capture spatial variability that is directly relevant to policy formulation and operational decision-making, rather than producing overly aggregated national estimates.

---

## 1.4 Study Objectives
The primary objectives of this project are to:
- Construct a high-quality, district-level spatio-temporal dataset integrating cholera surveillance data with climate and population covariates  
- Quantify the association between climate variables and cholera incidence using statistical models appropriate for count and rate data  
- Assess lagged effects of climatic factors to reflect delayed environmental influences on disease transmission  
- Develop an interactive visualization tool to communicate spatial and temporal patterns of cholera risk across Kenya  

---

## 1.5 Contribution of This Study
This project contributes to the existing literature by:
- Leveraging high-resolution climate reanalysis data (ERA5)  
- Integrating population-adjusted incidence measures  
- Applying Negative Binomial regression to address overdispersion in cholera count data  
- Translating analytical outputs into an interactive Streamlit-based application  

Beyond academic analysis, the project emphasizes **reproducibility, transparency, and practical usability**, aligning with modern standards in data science and applied public health research.

# Chapter 2 — Data Sources and Acquisition

## Overview
This study integrates multiple heterogeneous data sources spanning epidemiology, climate, population, and spatial boundaries. All datasets were selected based on credibility, spatial resolution, temporal coverage, and relevance to cholera transmission dynamics.

Data acquisition was conducted exclusively through open-access repositories and public APIs to ensure full reproducibility of the analytical pipeline.

---

## 2.1 Cholera Surveillance Data

### Source
- National and regional cholera surveillance datasets  
- Compiled and cleaned prior to this study

### Description
The cholera dataset contains reported cholera cases aggregated at the district (Admin-2) level, with temporal information recorded at weekly resolution. Key fields include:
- District name  
- Start and end dates of the reporting period  
- Total reported cholera cases  

### Pre-processing at Source Level
Prior to integration:
- Invalid or missing dates (`NaT`) were identified and removed  
- The dataset was restricted to Kenyan records only to ensure spatial consistency  
- Reporting periods were standardized to enable aggregation to monthly resolution  

### Rationale for Use
Cholera surveillance data serves as the response variable for all downstream modeling. District-level aggregation aligns directly with administrative units used for public health planning and outbreak response in Kenya.

> 📌 *Screenshot to be included in final version*  
> Raw cholera dataset preview (pre-cleaning)

---

## 2.2 Climate Data (ERA5 Reanalysis)

### Source
- Copernicus Climate Data Store (CDS)  
- Dataset: **ERA5 Monthly Reanalysis**

### Variables Extracted
- Mean air temperature  
- Total precipitation  
- Mean relative humidity  

### Spatial and Temporal Resolution
- Spatial: ~0.25° × 0.25° grid  
- Temporal: Monthly aggregates  
- Coverage: Entire Kenyan territory  

### Access Method
- Data accessed via the Copernicus CDS API  
- Downloaded in NetCDF (`.nc`) format  
- Converted to CSV for downstream processing  

### Rationale for Use
ERA5 provides physically consistent and globally validated climate estimates, making it a standard reference dataset in climate–health and environmental epidemiology research.

> 📌 *Screenshot to be included in final version*  
> ERA5 data download via CDS API

---

## 2.3 Population Data (WorldPop)

### Source
- WorldPop Project  

### Dataset
- Gridded Population of the World (PPP-adjusted)

### Description
WorldPop provides high-resolution raster estimates of population distribution derived from census data and ancillary geospatial covariates.

### Resolution
- Spatial: ~100 m raster grid  
- Temporal: Annual snapshot (2020)

### Processing Steps
- Raster clipped to Kenyan national boundaries  
- Zonal statistics computed using GADM Admin-2 polygons  
- District-level population totals and population density calculated  

### Rationale for Use
Population data is required to:
- Standardize cholera burden using incidence rates  
- Account for exposure heterogeneity across districts  

> 📌 *Screenshot to be included in final version*  
> WorldPop raster visualization over Kenya

---

## 2.4 Administrative Boundary Data (GADM)

### Source
- Global Administrative Areas (GADM) Database  

### Version
- GADM 4.1

### Administrative Level
- Admin Level 2 (Districts)

### Files Used
- Shapefiles (`.shp`, `.dbf`, `.shx`)  
- Converted to GeoJSON format for Streamlit deployment  

### Rationale for Use
Admin-2 boundaries:
- Match the spatial resolution of cholera reporting  
- Enable district-level spatial joins  
- Support geospatial visualization and statistical modeling  

> 📌 *Screenshot to be included in final version*  
> GADM Admin-2 boundaries map for Kenya

---

## 2.5 Data Integration Strategy
All datasets were harmonized to a common analytical structure defined by:
- **Spatial unit:** District (Admin-2)  
- **Temporal unit:** Month  
- **Coordinate reference system:** WGS 84 (EPSG:4326)

Integration steps included:
- Temporal aggregation of cholera cases from weekly to monthly resolution  
- Spatial aggregation of climate variables to district-level zonal means  
- Population normalization to compute incidence per 100,000 population  
- Manual and fuzzy matching of district names to ensure spatial consistency across datasets  

This process produced a single, modeling-ready spatio-temporal table suitable for statistical analysis and visualization.

---

## 2.6 Reproducibility and Data Management
All datasets are:
- Stored in a structured directory hierarchy  
- Loaded using explicit file paths  
- Version-controlled where possible  
- Accompanied by documented preprocessing steps  

The final cleaned dataset is exported as:

```text
kenya_cholera_modeling_table_cleaned.csv
```

# Chapter 3 — Data Preparation and Integration

## 3.1 Overview of the Data Pipeline
This study required the integration of multiple heterogeneous datasets differing in spatial resolution, temporal frequency, file formats, and naming conventions. As a result, data preparation constituted a substantial portion of the project and was critical to ensuring analytical validity.

The final modeling dataset was constructed through the sequential execution of the following steps:
- Data ingestion from multiple external sources  
- Temporal harmonization to a common monthly scale  
- Spatial harmonization at the district (Admin-2) level  
- Extensive cleaning and reconciliation of administrative names  
- Population normalization and incidence computation  
- Integration of lagged climate variables  

Each of these steps is described in detail below.

---

## 3.2 Cholera Surveillance Data Processing

### 3.2.1 Raw Data Structure
The cholera surveillance data were provided as country-specific CSV files containing weekly records with the following variables:
- Country  
- Epidemiological week  
- Start and end dates  
- Administrative location (district-level text labels)  
- Total reported cholera cases  

Temporal coverage spanned **2022–2024**, with varying completeness across districts.

---

### 3.2.2 Temporal Aggregation
Given the mismatch between weekly cholera reporting and monthly climate covariates, all cholera records were aggregated to a monthly resolution. Monthly aggregation was selected to:
- Reduce noise associated with irregular weekly reporting  
- Improve alignment with environmental covariates  
- Enhance statistical model stability  

For each district–month combination, total cholera cases were summed.

---

### 3.2.3 Handling Missing and Invalid Dates
During preprocessing, a small number of invalid date entries (`NaT`) were identified. These records were:
- Inspected manually  
- Confirmed to be non-recoverable  
- Removed to prevent temporal misalignment  

This step affected a negligible fraction of observations and did not materially bias spatial or temporal coverage.

---

## 3.3 Administrative Boundary Harmonization

### 3.3.1 GADM Shapefiles
District-level administrative boundaries were obtained from **GADM v4.1** (Admin-2 level for Kenya). These shapefiles served as the spatial backbone for:
- District name standardization  
- Population aggregation  
- Spatial visualization and joins  

---

### 3.3.2 District Name Standardization
A major challenge was the inconsistency between district names in the cholera surveillance data and official GADM administrative names. Identified issues included:
- Spelling variations  
- Legacy district names  
- Sub-county versus district naming  
- Administrative boundary changes  

To resolve this, a multi-stage approach was employed:
- Text normalization (lowercasing, whitespace trimming)  
- Fuzzy string matching to identify likely correspondences  
- Manual validation and correction using a curated mapping table  

This process resulted in a **100% match rate** between cholera records and official Admin-2 districts.

Manual intervention was deliberately retained where necessary to avoid silent misclassification—a common and dangerous shortcut in spatial epidemiological analyses.

---

## 3.4 Population Data Integration

### 3.4.1 WorldPop Raster Data
Population estimates were sourced from **WorldPop** gridded population rasters for Kenya. These data provide high-resolution population counts suitable for spatial aggregation.

---

### 3.4.2 Zonal Statistics
Population estimates were aggregated to the district level using zonal statistics, computing zonal mean population density for each Admin-2 polygon. This approach was selected to ensure:
- Consistency with raster resolution  
- Stability across irregular polygon sizes  
- Robustness to edge effects  

All districts were successfully assigned population estimates, with no missing values.

---

### 3.4.3 Incidence Calculation
Cholera incidence was computed as:

incidence = (reported cases / district population) × 100,000


This transformation produced a standardized response variable suitable for inter-district comparison and regression modeling.

---

## 3.5 Climate Data Processing

### 3.5.1 ERA5 Climate Reanalysis
Climate variables were sourced from the **Copernicus ERA5 reanalysis dataset**, accessed via the CDS API. The following variables were extracted:
- Mean 2 m air temperature  
- Total precipitation  
- Mean relative humidity  

All variables were processed at monthly resolution.

---

### 3.5.2 Unit Harmonization
To improve interpretability:
- Temperature values were converted from Kelvin to Celsius  
- Precipitation values were converted from meters to millimeters  

These transformations did not affect model behavior but substantially improved clarity for interpretation and reporting.

---

### 3.5.3 Lag Construction
To account for delayed environmental effects on cholera transmission, lagged versions of climate variables (e.g., 1-month lag) were constructed. Lagging was performed **within districts** to preserve temporal ordering and prevent information leakage.

---

## 3.6 Final Modeling Table
The final modeling table consists of **424 district–month observations** with the following structure:
- Spatial identifiers (GID_2, district name)  
- Temporal variables (year, month)  
- Response variable (cholera incidence)  
- Population covariates  
- Climate variables (current and lagged)  

The dataset contains:
- No missing values  
- Consistent spatial identifiers  
- Clearly defined variable roles  

This table represents the culmination of the data preparation phase and serves as the sole input for subsequent modeling and visualization.

---

## 3.7 Summary
The data preparation process was intentionally rigorous and conservative, prioritizing correctness over convenience. Particular care was taken to ensure:
- Accurate spatial alignment  
- Transparent handling of administrative inconsistencies  
- Proper normalization of disease counts  
- Documented unit transformations  

This foundation was essential for producing defensible statistical inferences and trustworthy visual outputs.


# Chapter 4 — Exploratory Data Analysis and Modeling Strategy

## 4.1 Purpose of Exploratory Analysis

Exploratory Data Analysis (EDA) was conducted to understand the statistical properties of the cholera incidence data and to inform appropriate model selection. The objectives of this phase were to:

- Examine the distribution of cholera incidence across districts and time
- Identify potential seasonality and temporal trends
- Assess relationships between cholera incidence and climate covariates
- Evaluate model assumptions prior to formal estimation

EDA was performed using the finalized modeling table described in Chapter 3.

## 4.2 Distribution of Cholera Incidence

### 4.2.1 Skewness and Overdispersion

The cholera incidence variable exhibited:

- Strong right skew
- A high proportion of low or zero values
- Occasional extreme outbreaks

These characteristics are inconsistent with the assumptions of Gaussian regression and indicate count overdispersion, where the variance exceeds the mean.

### 4.2.2 Zero Inflation Assessment

While many district–month observations recorded zero cases, zeros were not structurally dominant. Most districts recorded at least one non-zero observation during the study period. This pattern suggests excess zeros driven by stochastic disease absence, rather than a structurally zero-generating process.

As a result:

- Zero-inflated models were considered
- However, a standard Negative Binomial model was deemed sufficient as a baseline

## 4.3 Temporal Patterns and Seasonality

### 4.3.1 Monthly Seasonality

Visual inspection of monthly incidence patterns revealed moderate seasonality, characterized by:

- Increased incidence during wetter months
- Reduced incidence during drier periods

Seasonality was present but not uniform across districts, suggesting interaction between local environmental and socio-demographic conditions.

### 4.3.2 Interannual Variation

Cholera incidence varied between years, with certain years exhibiting more widespread outbreaks. However, no monotonic trend was observed across the study period, supporting the inclusion of year indicators rather than a continuous trend term.

## 4.4 Climate Covariate Relationships

### 4.4.1 Temperature

Mean monthly temperature showed a consistent positive association with cholera incidence. Higher temperatures were visually associated with increased incidence, consistent with known biological and environmental mechanisms influencing *Vibrio cholerae* persistence.

### 4.4.2 Precipitation

Precipitation exhibited a non-linear relationship with incidence:

- Low precipitation was associated with reduced incidence
- Moderate to high precipitation corresponded to increased outbreak risk

This supports hypotheses linking rainfall to water contamination and infrastructure stress.

### 4.4.3 Relative Humidity

Relative humidity showed a negative association with cholera incidence. While statistically significant, its biological interpretation is less direct and may reflect correlated climatic regimes rather than a causal mechanism.

## 4.5 Model Selection Rationale

### 4.5.1 Rejection of Linear Models

Linear regression was deemed inappropriate due to:

- Non-normality of residuals
- Heteroskedasticity
- Inability to handle count-based variance structures

### 4.5.2 Poisson vs Negative Binomial

A Poisson regression model assumes equality of mean and variance. Preliminary diagnostics revealed substantial overdispersion, violating this assumption.

The Negative Binomial (NB) model was therefore selected as it:

- Explicitly models overdispersion
- Is well-established in epidemiological count modeling
- Provides interpretable incidence rate ratios (IRRs)

### 4.5.3 Baseline Model Specification

The baseline NB model included:

- Cholera incidence as the response variable
- Climate covariates (temperature, precipitation, humidity)
- Population normalization via incidence formulation
- Temporal controls (year and month)

Lagged climate terms were introduced in subsequent model refinements to capture delayed effects.

## 4.6 Interpretation of Incidence Rate Ratios

Model coefficients were interpreted as Incidence Rate Ratios (IRRs):

- IRR > 1 indicates increased risk
- IRR < 1 indicates reduced risk

This framing allows for intuitive interpretation of climate effects on cholera transmission risk.

## 4.7 Summary

The EDA phase established that:

- Cholera incidence is overdispersed and right-skewed
- Moderate seasonality is present
- Climate variables exhibit meaningful associations
- Negative Binomial regression is an appropriate modeling framework

These findings informed the modeling approach implemented in the subsequent chapter.
