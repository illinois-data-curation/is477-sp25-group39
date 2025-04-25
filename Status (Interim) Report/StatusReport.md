# Status Report: Mental Health and Academic Performance Analysis

## Project Overview
This project investigates the relationship between student academic performance and mental health, focusing on depression. Using two distinct datasets from Kaggle, the analysis aims to identify factors influencing student mental health and develop a predictive model for depression risk. The methodology involves data acquisition, cleaning, exploration, visualization, and modeling.

## Progress by Task

### 1. Data Acquisition & Integrity Checks ✅
- Both datasets have been successfully downloaded and reviewed.
  - **Student Depression Dataset** (CSV)
  - **Student Performance & Behavior Dataset** (JSON → converted to CSV)
- Conversion of the JSON dataset was performed using `pandas.json_normalize()`.
- Both datasets were saved and documented in `data_acquisition.ipynb`.

### 2. Data Cleaning & Preprocessing ✅
- Standardized column names across datasets.
- Missing values handled using median/mode imputation (numeric/categorical respectively).
- Dataset shapes and summaries are included in `data_cleaning_preprocessing.ipynb`.

### 3. Data Profiling & EDA ✅
- Conducted EDA for both datasets in `eda_visualizations.ipynb`.
- Key insights include:
  - Financial stress and sleep duration strongly relate to depression indicators.
  - Higher attendance and performance relate to lower reported stress.
- Plotted heatmaps and boxplots for core variables (e.g., CGPA vs. depression).

### 4. Feature Engineering & Initial Modeling ✅
- Binary encoding of categorical features completed.
- Used one-hot encoding and feature scaling with `StandardScaler`.
- Trained Random Forest and Logistic Regression models using stratified train-test split.
  - Random Forest: ~0.81 accuracy, ~0.84 AUC
- Model evaluation included classification report and confusion matrix.
- Code and results are documented in `model_dev_baseline.ipynb`.

### 5. Project Repository Setup ✅
- All files and artifacts are being committed to GitHub.
- File structure follows reproducibility best practices.
- `requirements.txt` lists project dependencies.

## Timeline Updates
| Date        | Task Completed                                                  | Status       |
|-------------|------------------------------------------------------------------|--------------|
| Mar 13      | Team selection                                                  | ✅ Done       |
| Mar 21-28   | Data acquisition & conversion                                   | ✅ Done       |
| Mar 29-Apr 2| Project plan submission                                         | ✅ Done       |
| Apr 3-10    | Data cleaning, preprocessing, and EDA                          | ✅ Done       |
| Apr 11-14   | Feature engineering & model development                         | ✅ Done       |
| Apr 15-24   | Model tuning, additional visualizations                         | 🚧 In progress|
| Apr 26-30   | Final documentation & GitHub prep                               | 🔜 Upcoming   |
| May 1       | Final submission                                                | 🔜 Upcoming   |

## Changes to Original Plan
- Due to a lack of a shared identifier between the two datasets, direct merging was not feasible. Instead, parallel analysis was performed.
- Rather than full integration, feature overlap was leveraged to draw thematic connections (e.g., stress, sleep, and academic performance).
- Replaced SMOTE with a more curriculum-aligned stratified split and scaling approach using `StandardScaler` and `train_test_split`.

## Artifacts in GitHub Repository 
- `data_acquisition.ipynb`: Data loading and inspection
- `data_cleaning_preprocessing.ipynb`: Cleaning, preprocessing
- `eda_visualizations.ipynb`: Correlation plots, insights
- `model_dev_baseline.ipynb`: Model training and evaluation using UIUC-aligned practices
- `requirements.txt`: Project dependencies
- `README.md`: Project overview, structure, setup

## Next Steps
- Final model tuning using cross-validation and GridSearch
- Incorporate feature importance analysis (e.g., SHAP values)
- Begin drafting final report (`README.md`)
- Package workflows and upload results/output to Box for final submission
- Archive on Zenodo and finalize metadata

---
**Status Report Prepared by:** Shivali Patel

**GitHub Repository:** https://github.com/illinois-data-curation/is477-sp25-group39

**Tag to Create:** `status-report`
