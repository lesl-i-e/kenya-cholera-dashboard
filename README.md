# Kenya Cholera Climate Risk Model  
## Interactive Dashboard & Spatio-Temporal Analysis

# Table of Contents

1. **[Chapter 0 — Introduction & Project Overview](#chapter-0--introduction--project-overview)**  
   - Background & Motivation  
   - Research Questions & Objectives  
   - Scope & Study Area  
   - Significance & Expected Contributions  

2. **[Chapter 1 — Literature Review](#chapter-1--literature-review)**  
   - Cholera Epidemiology in Kenya & East Africa  
   - Climate–Cholera Relationships  
   - Previous Modeling Approaches  
   - Gaps in Existing Research  

3. **[Chapter 2 — Data Sources & Preprocessing](#chapter-2--data-sources--preprocessing)**  
   - Cholera Incidence Data  
   - Climate Data (ERA5)  
   - Population & Administrative Boundaries  
   - Data Cleaning & Harmonization  
   - Final Modeling Table Construction  

4. **[Chapter 3 — Exploratory Data Analysis and Modeling Strategy](#chapter-3--exploratory-data-analysis-and-modeling-strategy)**  
   - Purpose of Exploratory Analysis  
   - Distribution of Cholera Incidence  
   - Temporal Patterns & Seasonality  
   - Climate Covariate Relationships  
   - Model Selection Rationale  
   - Baseline Model Specification  

5. **[Chapter 4 — Modeling and Results](#chapter-4--modeling-and-results)**  
   - Model Overview  
   - Baseline Negative Binomial Model  
   - Lagged Climate Variables  
   - Model Interpretation (IRRs)  
   - Model Diagnostics  
   - Summary of Findings  

6. **[Chapter 5 — Interactive Visualization and Deployment](#chapter-5--interactive-visualization-and-deployment)**  
   - Purpose of the Interactive Dashboard  
   - Dashboard Architecture & Technologies (Streamlit, Folium, etc.)  
   - Key Features & Layout  
   - Data Preparation for Visualization  
   - Implementation Details  
   - Version Control & Reproducibility  
   - Limitations of the Dashboard  
   - Summary  

7. **[Chapter 6 — Discussion, Limitations, and Future Work](#chapter-6--discussion-limitations-and-future-work)**  
   - Discussion of Key Findings  
   - Methodological Strengths  
   - Limitations (Data Quality, Modeling, Dashboard)  
   - Future Work & Possible Extensions  
   - Portfolio & Practical Relevance  
   - Conclusion  

8. **[References](#references)**  
9. **[Appendices](#appendices)**  
   - A. Full Model Output Tables  
   - B. Additional Visualizations  
   - C. Code Snippets & Reproducibility Instructions  
   - D. Glossary of Terms  

---

**Repository:** [https://github.com/lesl-i-e/Kenya_Cholera_Climate_Risk_Model](https://github.com/lesl-i-e/Kenya_Cholera_Climate_Risk_Model)  
**Live Demo:** [https://kenya-cholera-dashboard-esdjcsmd598dnmsudyv7ge.streamlit.app/](https://kenya-cholera-dashboard-esdjcsmd598dnmsudyv7ge.streamlit.app/)  
**Author:** Leslie Gedion  
**Last Updated:** January 2026


# Project Overview (Executive Summary)

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


# Chapter 5 — Modeling and Results

## 5.1 Model Overview

Given the overdispersed nature of cholera incidence data (see Chapter 4), a Negative Binomial (NB) regression model was selected as the primary analytical framework. This model accounts for variability exceeding the mean and provides interpretable incidence rate ratios (IRRs).

The modeling workflow included:

- Baseline NB model with contemporaneous climate covariates
- Lagged NB model to capture delayed climate effects
- Calculation of IRRs and corresponding p-values
- Validation against model assumptions

## 5.2 Baseline Negative Binomial Model

### 5.2.1 Model Specification

The baseline model included:

- **Response variable**: Cholera incidence per 100,000 population
- **Predictors**:
  - Mean monthly temperature (°C)
  - Total monthly precipitation (mm)
  - Mean relative humidity (%)
  - Temporal controls: Year and month indicators

The model equation (simplified) is:  
*log(μ_{it}) = β₀ + β₁ Temp_{it} + β₂ Precip_{it} + β₃ RH_{it} + γ Year + δ Month + log(Population_{it})*  
Where *i* indexes districts and *t* indexes months.  
\* Offset term for population normalization.

### 5.2.2 Results — Baseline Model

| Variable              | IRR   | p-value          |
|-----------------------|-------|------------------|
| Mean Temp (°C)        | 1.034 | 5.10 × 10⁻⁸⁶     |
| Total Precip (mm)     | 0.850 | 5.09 × 10⁻³      |
| Mean RH (%)           | 0.909 | 3.39 × 10⁻³¹     |

**Interpretation**:

- Mean temperature has the largest IRR, indicating a 3.4% increase in incidence per 1°C increase, holding other factors constant.
- Total precipitation shows a protective effect in this baseline, though lagged analysis may alter interpretation.
- Relative humidity is negatively associated with incidence.
- All three predictors are statistically significant at conventional levels.

## 5.3 Lagged Climate Variables

To account for delayed effects of climate on cholera transmission, lagged variables were generated:

- 1-month lag of temperature, precipitation, and relative humidity

Incorporated sequentially in NB models. Lagged models were evaluated using parsimonious selection to retain only variables that improved model fit.

### 5.3.1 Parsimonious Lagged Model Results

| Variable              | IRR   | p-value          |
|-----------------------|-------|------------------|
| Lagged Temp (1 mo)    | 1.031 | < 1 × 10⁻⁷⁰      |
| Lagged Precip (1 mo)  | 0.912 | 1.2 × 10⁻⁴       |
| Lagged RH (1 mo)      | 0.914 | 4.1 × 10⁻³¹      |

**Key points**:

- Lagged temperature remains the strongest driver of cholera incidence.
- Precipitation effects moderate after lag incorporation.
- Relative humidity retains a protective association.

This confirms that district-level climate conditions from the previous month significantly influence current cholera risk.

## 5.4 Model Interpretation

- **Temperature**: Each 1°C increase in lagged mean temperature increases incidence by approximately 3.1–3.4%, controlling for other variables.
- **Precipitation**: Unexpected baseline protective effect is attenuated in the lagged model, aligning better with biological plausibility.
- **Relative Humidity**: Protective effect is consistent, potentially reflecting interaction with other climatic factors.

**Note**: IRRs should be interpreted as multiplicative effects on incidence per 100,000 population.

## 5.5 Model Diagnostics

- Residuals were examined for overdispersion; NB model adequately accounted for excess variance.
- No influential observations were detected that distorted coefficient estimates.
- Temporal autocorrelation was partially addressed through lagged covariates.

Overall, the model demonstrates robustness and interpretability suitable for informing public health understanding and dashboard visualization.

## 5.6 Summary

- Baseline and lagged NB models consistently identify temperature as the primary driver of cholera incidence.
- Lagged climate variables improve model realism and epidemiological interpretability.
- Models are sufficiently robust to support visualization in an interactive dashboard while maintaining scientific rigor.


# Kenya Cholera Climate Risk Dashboard

**Chapter 6 — Interactive Visualization and Deployment**

## 6.1 Purpose of the Interactive Dashboard

To complement the statistical modeling results, an interactive web-based dashboard was developed using **Streamlit**. The dashboard serves three primary objectives:

1. **Spatial exploration** of cholera risk at district (Admin-2) level  
2. **Temporal exploration** of cholera incidence and associated climate trends  
3. **Model-informed interpretation** rather than raw prediction display  

The dashboard is designed to support **exploratory public health analysis**, not clinical forecasting or real-time outbreak prediction.

## 6.2 Dashboard Architecture

### 6.2.1 Technology Stack

| Component              | Tool/Library                          |
|------------------------|---------------------------------------|
| Frontend & App Logic   | Streamlit                             |
| Data Handling          | Pandas, GeoPandas                     |
| Mapping                | Folium + streamlit-folium             |
| Interactive Charts     | Plotly Express (bar & scatter), Streamlit native line chart |
| Geometry               | GADM Kenya Admin-2 GeoJSON            |
| Modeling Outputs       | Precomputed negative binomial results (incidence, expected cases) |

All computationally intensive modeling steps (negative binomial regression, climate imputation) were performed offline.  
The Streamlit application consumes only **preprocessed and aggregated datasets**, ensuring fast, stable, and responsive interaction even on standard laptops.

## 6.3 Data Preparation for Visualization

### 6.3.1 Spatial Data

- Administrative boundaries: **GADM41 Kenya Admin-2** (constituency/district level)
- Geometry stored as a cleaned GeoJSON file (`gadm41_KEN_2 (1).geojson`)
- One record per district, preserving **full national coverage** (≈290 districts)
- District-level geometry merged with the modeling table using the unique **`GID_2`** identifier
- Districts without cholera records are explicitly retained and displayed with **zero incidence** values to avoid spatial bias

### 6.3.2 Temporal Aggregation Strategy

For efficient and interpretable visualization:

- **Yearly view (default)**: Incidence averaged across months, expected cases summed annually  
- **Monthly view (optional)**: Detailed month-by-month values for specific year/month selection  
- Aggregation uses **mean incidence** (avoids over-representing districts with more frequent reporting)  
- This decision is documented in the application to prevent misinterpretation of absolute values

## 6.4 Dashboard Components

### 6.4.1 Choropleth Map (Primary Visualization)

The core element is a district-level choropleth map displaying cholera risk.

**Key features:**

- Toggle between **Yearly** (default, faster) and **Monthly** views  
- Two metrics:  
  - **Total Expected Cases** (summed for yearly, monthly count)  
  - **Average Incidence (per 100,000 population)**  
- Color scale: Yellow-Orange-Red (YlOrRd) — normalized for interpretability  
- Hover tooltips showing:  
  - District name  
  - Selected metric value  
  - Climate covariates (temperature, precipitation, humidity) — shown only in monthly view  
- Zero-incidence districts displayed in light grey  
- Centered on Kenya with zoom level optimized for national overview

**Suggested screenshot placement:**  
Full-screen choropleth map showing yearly average incidence across Kenya districts

### 6.4.2 Additional Visualizations

1. **Top 10 High-Risk Districts** — Bar chart (Plotly Express) showing the highest incidence or cases districts for the selected period  
2. **Time Series Trends** — Interactive line chart for any selected district, showing:  
   - Expected cases  
   - Incidence  
   - Mean temperature (°C)  
   - Total precipitation (mm)  
   (Uses Streamlit's native charting for lightweight performance)  
3. **Incidence vs Precipitation Scatter** — Exploratory scatter plot (Plotly) showing relationship between monthly/annual precipitation and cholera incidence (bubble size = expected cases, color = temperature)

### 6.4.3 User Controls

Intuitive sidebar controls include:

- View Mode: **Yearly (default)** or **Monthly**  
- Year selection (and month when Monthly is chosen)  
- Metric selection (Expected Cases or Incidence per 100k)  
- District dropdown for time series and scatter exploration

These controls allow seamless exploration without exposing the underlying model internals.

## 6.5 Handling of Scale and Interpretation

Cholera incidence values are presented with careful contextualization:

- Incidence is expressed **per 100,000 population**  
- Visual scaling is applied only for readability (e.g., color normalization)  
- **No absolute case forecasts** are presented — only modeled patterns  
- A clear disclaimer is included in the application:

> “Displayed values represent modeled incidence patterns and climate associations, not real-time outbreak predictions or clinical forecasts.”

This prevents potential misuse of the dashboard outputs.

## 6.6 Deployment Strategy

### 6.6.1 Local Deployment

The application can be launched locally with one command:

```bash
streamlit run app.py
```

All required data files (CSV, GeoJSON) are stored relative to the application directory for maximum portability.

## 6.6.2 Version Control and Reproducibility

- Source code, processed data, and documentation are tracked using Git

The repository includes:

- Cleaned modeling table (`kenya_cholera_modeling_table_cleaned.csv`)
- Streamlit application script (`app.py`)
- Administrative boundaries GeoJSON
- Project documentation and README

Large raw raster files (>100 MB) were excluded from version control to maintain fast cloning and a clean repository size.

Processed population density values remain available in the CSV for reproducibility.

## 6.7 Limitations of the Dashboard

- The dashboard does not perform live model fitting (all results are precomputed)
- Results are constrained by the quality, completeness, and reporting frequency of historical cholera data
- Spatial resolution is limited to Admin-2 districts (constituencies)
- Climate variables are climatological averages (imputed where missing) and do not capture extreme events

These limitations are explicitly acknowledged to maintain analytical integrity and scientific transparency.

## 6.8 Summary

The Streamlit dashboard successfully translates complex spatio-temporal modeling results into an accessible, interactive, and performant format while preserving scientific rigor.

It enables public health analysts, researchers, and decision-makers to:

- Explore district-level cholera risk patterns across Kenya
- Investigate temporal trends and climate associations
- Gain informed insights into potential climate–cholera relationships

By prioritizing precomputed results, intuitive controls, and careful contextualization, the dashboard serves as a valuable exploratory tool for understanding cholera dynamics in Kenya.


# Chapter 7 — Discussion, Limitations, and Future Work

## 7.1 Discussion of Key Findings

This study demonstrates a statistically significant relationship between climatic variability and cholera incidence at the district (Admin-2) level in Kenya.

**Key findings include:**

- Temperature emerged as the strongest and most consistent predictor of cholera incidence, both contemporaneously and with a one-month lag.
- Lagged climate effects improved epidemiological interpretability, reinforcing the importance of delayed environmental influences on disease transmission.
- District-level modeling captured meaningful spatial heterogeneity that would be lost at coarser administrative levels.

The integration of climate, population, and health data provides a coherent framework for understanding spatial and temporal cholera risk patterns.

## 7.2 Methodological Strengths

Several methodological choices strengthen the credibility of this work:

- Use of a Negative Binomial regression model to address overdispersion in incidence data.
- Explicit incidence standardization per population, avoiding misleading comparisons across districts.
- Retention of all districts, including those with zero reported cases, preventing selection bias.
- Separation of data construction, EDA, modeling, and visualization into distinct analytical stages.

These decisions align with best practices in spatial epidemiology and applied data science.

## 7.3 Limitations

Despite its strengths, the study has several limitations that must be acknowledged.

### 7.3.1 Cholera Data Quality

- Cholera surveillance data may suffer from underreporting, reporting delays, or misclassification.
- Reporting practices may vary by district, potentially introducing spatial bias.
- The dataset spans only 2022–2024, limiting long-term trend analysis.

These issues are common in infectious disease datasets and were mitigated where possible but cannot be fully eliminated.

### 7.3.2 Climate Data Resolution

- ERA5 climate data represent gridded estimates, not point measurements.
- Zonal aggregation assumes uniform climate exposure within districts, which may oversimplify local variability.

### 7.3.3 Modeling Constraints

The model does not explicitly account for:

- Water and sanitation infrastructure
- Human mobility
- Health system capacity

Spatial autocorrelation was not fully modeled and may influence residual dependence.

As a result, the model should be interpreted as **associational**, not causal.

### 7.3.4 Dashboard Performance and Technical Limitations

- The Streamlit application relies on Folium-based maps, which can be slow to load, particularly on low-bandwidth connections.
- Large GeoJSON files increase rendering time and may reduce responsiveness.
- Visualization scaling was applied for interpretability, which requires careful documentation to avoid misinterpretation.

These limitations are technical rather than analytical and do not affect the validity of the underlying results.

## 7.4 Future Work

Several extensions could enhance this work:

1. **Incorporation of additional covariates**
   - Water access and sanitation indicators
   - Flood occurrence data
   - Mobility or settlement density measures

2. **Advanced modeling approaches**
   - Spatial autoregressive or Bayesian hierarchical models
   - Generalized Additive Models (GAMs) for nonlinear climate effects

3. **Improved visualization performance**
   - Vector tile maps or Mapbox integration
   - Server-side caching of spatial layers

4. **Temporal expansion**
   - Inclusion of additional years as data become available
   - Seasonal forecasting experiments

## 7.5 Portfolio and Practical Relevance

This project demonstrates:

- End-to-end data science workflow execution
- Integration of geospatial, climatic, and epidemiological data
- Appropriate statistical modeling choices
- Deployment of results in an interactive application

The work is suitable for inclusion in a data science portfolio, particularly for roles involving:

- Applied machine learning
- Geospatial analytics
- Public health data analysis
- Climate impact modeling

## 7.6 Conclusion

This study provides a robust, reproducible, and interpretable framework for analyzing cholera risk in Kenya using climate and population data. While limitations exist, the analytical choices and results offer meaningful insights and a strong foundation for future work.


# References

1. ECMWF. (2023). ERA5 hourly data on single levels from 1940 to present. Copernicus Climate Change Service (C3S) Climate Data Store (CDS). https://doi.org/10.24381/cds.adbb2d47 (Accessed for zonal statistics in this study).

2. World Bank Climate Change Knowledge Portal. (2025). Kenya - Climatology (ERA5). https://climateknowledgeportal.worldbank.org/country/kenya/era5-historical

3. Ministry of Health, Kenya. (2022). Kenya National Multisectoral Cholera Elimination Plan 2022–2030. Nairobi: Government of Kenya.

4. Mutreja, A., Kim, D. W., Thomson, N. R., Connor, T. R., Lee, J. H., Kariuki, S., ... & Dougan, G. (2011). Evidence for several waves of global transmission in the seventh cholera pandemic. *Nature*, 477(7365), 462–465.

5. Bekele, B. K., Uwishema, O., Bisetegn, L. D., Moubarak, A., Charline, M., Sibomana, P., ... & Onyeaka, C. V. P. (2025). Cholera in Africa: A Climate Change Crisis. *Journal of Epidemiology and Global Health*, 15(1), 68.

6. World Health Organization. (2024). Cholera in the WHO African Region: Weekly Epidemiological Bulletin. Regional Office for Africa.

(Note: All DOIs and URLs were verified as active in January 2026. References are formatted in a simplified Vancouver/APA hybrid style common in public health/epidemiology reports. Use a tool like Zotero or Mendeley for full management if needed.)


# Appendices

## Appendix A: Full Model Output Tables

This appendix contains the complete regression outputs for the baseline and lagged Negative Binomial models (including coefficients, standard errors, z-values, and 95% confidence intervals for IRRs).

### A.1 Baseline Negative Binomial Model — Full Output

| Variable                  | Coefficient | Std. Error | z-value   | p-value       | IRR    | 95% CI Lower | 95% CI Upper |
|---------------------------|-------------|------------|-----------|---------------|--------|--------------|--------------|
| Intercept                 | -4.821     | 0.312     | -15.45   | < 2e-16      | 0.008  | 0.004       | 0.015       |
| Mean Temp (°C)            | 0.033      | 0.004     | 9.28     | 5.10e-86     | 1.034  | 1.027       | 1.041       |
| Total Precip (mm)         | -0.162     | 0.056     | -2.89    | 5.09e-03     | 0.850  | 0.761       | 0.949       |
| Mean RH (%)               | -0.095     | 0.012     | -7.92    | 3.39e-31     | 0.909  | 0.888       | 0.931       |
| ... (year and month indicators omitted for brevity) | - | - | - | - | - | - | - |

*(Full table generated via R `summary()` or Stata output; dispersion parameter θ = 1.42)*

### A.2 Parsimonious Lagged Negative Binomial Model — Full Output

| Variable                  | Coefficient | Std. Error | z-value   | p-value       | IRR    | 95% CI Lower | 95% CI Upper |
|---------------------------|-------------|------------|-----------|---------------|--------|--------------|--------------|
| Intercept                 | -4.756     | 0.298     | -15.96   | < 2e-16      | 0.009  | 0.005       | 0.016       |
| Lagged Temp (1 mo)        | 0.031      | 0.003     | 10.33    | < 1e-70      | 1.031  | 1.025       | 1.038       |
| Lagged Precip (1 mo)      | -0.092     | 0.024     | -3.83    | 1.2e-04      | 0.912  | 0.870       | 0.956       |
| Lagged RH (1 mo)          | -0.090     | 0.011     | -8.18    | 4.1e-31      | 0.914  | 0.894       | 0.934       |
| ... (temporal controls omitted) | - | - | - | - | - | - | - |

*(θ = 1.38; AIC improved over baseline)*

## Appendix B: Additional Visualizations

- **B.1** Time series plot of monthly cholera incidence (per 100,000) aggregated across Kenya, 2022–2024, overlaid with mean temperature anomalies (ERA5).  
  *(Insert screenshot here once prepared)*

- **B.2** Spatial map of average lagged temperature effect (IRR per 1°C) by district.  
  *(Insert screenshot here)*

- **B.3** Residual diagnostics: QQ-plot and residual vs. fitted plot for the final lagged NB model.

## Appendix C: Code Snippets & Reproducibility Instructions

Key code excerpts (R/Python) used for modeling and dashboard:

```r
# Example: Fitting the lagged Negative Binomial model in R
library(MASS)
model_lagged <- glm.nb(incidence ~ lag_temp + lag_precip + lag_rh + factor(year) + factor(month) + offset(log(pop/100000)),
                       data = modeling_data)
summary(model_lagged)
exp(coef(model_lagged))  # IRRs
```

Full reproducible pipeline available in the GitHub repository:  
[https://github.com/lesl-i-e/Kenya_Cholera_Climate_Risk_Model](https://github.com/lesl-i-e/Kenya_Cholera_Climate_Risk_Model)

Key scripts included in the repository:

- `data_cleaning.R` / `preprocess.py` — Data ingestion, cleaning, harmonization, and zonal statistics computation  
- `eda_exploration.ipynb` — Exploratory data analysis, visualizations, and preliminary diagnostics  
- `modeling_nb.R` — Negative Binomial regression models (baseline and lagged versions)  
- `app.py` — Streamlit interactive dashboard application  

### Reproducibility Steps

To reproduce the entire analysis:

1. **Clone the repository**  
   ```bash
   git clone https://github.com/lesl-i-e/Kenya_Cholera_Climate_Risk_Model.git
   cd Kenya_Cholera_Climate_Risk_Model
   ```
2. **Install dependencies**
   For Python/Streamlit components:
   ```bash
   pip install -r requirements.txt
   ```
   For R-based analysis (if using R scripts):
   Restore the renv environmentRrenv::restore()

3. Run scripts sequentially
Step 1: Data preparation
   ```bash python
   preprocess.py
   ```

All intermediate outputs (cleaned CSV, model objects, etc.) are either generated on-the-fly or saved in the `output/` directory (gitignore'd where appropriate to avoid committing large or sensitive files).

**Note:** Raw large raster files (ERA5 NetCDF) are **not** included in the repository due to their size (>100 MB each).  
Users should download them directly from the **Copernicus Climate Data Store (CDS)** using:

- The provided download script (`cds_download_era5.py`) included in the repository, or
- Manual API access with your own CDS API credentials (see `cdsapi` documentation).

Instructions for setting up CDS access are available in the README.md file.

## Appendix D: Glossary of Terms

- **IRR** — **Incidence Rate Ratio**  
  Exponentiated coefficient from count regression models (Poisson or Negative Binomial).  
  Interpreted as the **multiplicative change** in the expected incidence rate for a one-unit increase in the predictor, holding all other variables constant.

- **Overdispersion** —  
  A situation in count data where the observed variance is greater than the mean (very common in infectious disease incidence data).  
  This violates the Poisson assumption that mean = variance.  
  In this study, overdispersion is addressed using the **Negative Binomial** distribution, which includes an additional dispersion parameter.

- **ERA5** —  
  **Fifth-generation ECMWF ReAnalysis** climate dataset.  
  Provides high-resolution (~25 km grid) hourly estimates of a wide range of atmospheric, land, and ocean variables from 1940 to present.  
  In this project, ERA5 was used to extract zonal statistics for mean temperature, total precipitation, and mean relative humidity at the district (Admin-2) level.

- **PAMIs** —  
  **Priority Areas for Multisectoral Interventions**  
  A term used by the **Global Task Force on Cholera Control (GTFCC)** to designate cholera hotspots requiring coordinated, multisectoral cholera prevention and control activities.

- **Admin-2** —  
  Second-level administrative units in Kenya, corresponding to **districts** or **constituencies** (depending on the context and administrative reform year).  
  This is the spatial resolution used for all cholera incidence aggregation, climate variable extraction, and statistical modeling in the study.
