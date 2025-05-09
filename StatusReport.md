# Status Report: Mental Health and Academic Performance Analysis

## Project Overview
This project explores the complex relationship between student academic performance and mental health, with a particular focus on depression among students. The analysis leverages two distinct datasets sourced from Kaggle: one centered on student depression indicators, and another capturing broader aspects of student performance and behavior. The overarching objective is twofold: to identify key factors that influence student mental health, and to develop a predictive model capable of assessing depression risk based on academic and behavioral data.

The methodology for this project is structured and comprehensive. It includes data acquisition, data cleaning and preprocessing, exploratory data analysis (EDA), feature engineering, model development, and evaluation. Each stage is meticulously documented, ensuring transparency and reproducibility throughout the analytical workflow. The project also emphasizes best practices in data science, such as maintaining a well-organized repository, using version control, and adhering to reproducibility standards.

## Progress by Task

### 1. Data Acquisition & Integrity Checks
The first phase of the project involved the successful acquisition and initial review of both datasets. The **Student Depression Dataset** was obtained in CSV format, while the **Student Performance & Behavior Dataset** was originally in JSON format and subsequently converted to CSV using the `pandas.json_normalize()` function. This conversion facilitated easier manipulation and analysis in subsequent stages. All data files were saved and documented in the `data_acquisition.ipynb` notebook, ensuring a clear record of the data sources and formats used.

Integrity checks were performed to verify the completeness and consistency of the data. This included inspecting for duplicate entries, ensuring proper data types, and confirming the presence of expected variables. These steps were critical in laying a solid foundation for the subsequent cleaning and analysis phases.

### 2. Data Cleaning & Preprocessing
Data cleaning and preprocessing were carried out systematically to ensure the datasets were suitable for analysis. Column names were standardized across both datasets to facilitate parallel analysis and thematic comparisons. Missing values were addressed using median imputation for numeric variables and mode imputation for categorical variables, minimizing the risk of bias that can arise from improper handling of incomplete data.

The shapes and summaries of the cleaned datasets were documented in `data_cleaning_preprocessing.ipynb`, providing transparency regarding the structure and content of the data. These steps ensured that the datasets were both reliable and ready for detailed exploration.

### 3. Data Profiling & Exploratory Data Analysis (EDA)
Exploratory data analysis was conducted for both datasets, with results and visualizations documented in `eda_visualizations.ipynb`. The EDA phase yielded several key insights:

- **Financial stress and sleep duration emerged as strong correlates of depression indicators**. Students experiencing higher financial stress or insufficient sleep tended to report more symptoms of depression.
- **Academic performance and attendance were inversely related to reported stress levels**. Students with higher grades and better attendance generally reported lower stress and fewer mental health concerns.
- Visualizations such as heatmaps and boxplots were generated to illustrate relationships between core variables, such as CGPA (Cumulative Grade Point Average) and depression scores.

These findings provided valuable context for feature engineering and model development, highlighting the importance of both academic and non-academic factors in student mental health.

### 4. Feature Engineering & Initial Modeling
Feature engineering was performed to prepare the data for machine learning models. Categorical features were binary encoded, and one-hot encoding was applied where appropriate. Feature scaling was conducted using `StandardScaler` to ensure that all variables contributed equally to the model.

Two baseline models were trained: **Random Forest** and **Logistic Regression**. A stratified train-test split was used to preserve the distribution of the target variable (depression risk) in both training and test sets. The Random Forest model achieved approximately 0.81 accuracy and an AUC (Area Under the Curve) of around 0.84, indicating strong predictive performance. Model evaluation included classification reports and confusion matrices to assess precision, recall, and overall effectiveness.

All code and results from this phase are documented in `model_dev_baseline.ipynb`, ensuring reproducibility and ease of review.

### 5. Project Repository Setup
The project repository is structured according to best practices for reproducibility and collaboration. All files, notebooks, and artifacts are regularly committed to GitHub. The repository includes a `requirements.txt` file listing all project dependencies, a `README.md` providing an overview and setup instructions, and dedicated notebooks for each stage of the workflow. This organization facilitates collaboration, version control, and future extensions of the project.

## Timeline Updates
The project has progressed according to the planned timeline, with most major milestones completed on schedule:

| Date        | Task Completed                                                  | Status       |
|-------------|------------------------------------------------------------------|--------------|
| Mar 13      | Team selection                                                  | ✅ Done       |
| Mar 21-28   | Data acquisition & conversion                                   | ✅ Done       |
| Mar 29-Apr 2| Project plan submission                                         | ✅ Done       |
| Apr 3-10    | Data cleaning, preprocessing, and EDA                           | ✅ Done       |
| Apr 11-14   | Feature engineering & model development                         | ✅ Done       |
| Apr 15-24   | Model tuning, additional visualizations                         | 🚧 In progress|
| Apr 26-30   | Final documentation & GitHub prep                               | 🔜 Upcoming   |
| May 1       | Final submission                                                | 🔜 Upcoming   |

## Changes to Original Plan
Several adjustments were made to the original project plan based on practical considerations:

- **Dataset Integration:** The absence of a shared identifier between the two datasets made direct merging infeasible. Instead, analyses were conducted in parallel, leveraging overlapping features such as stress, sleep, and academic performance to draw thematic connections.
- **Resampling Strategy:** The initial plan to use SMOTE (Synthetic Minority Over-sampling Technique) for handling class imbalance was replaced with a stratified train-test split and feature scaling, aligning better with curriculum requirements and ensuring a more robust evaluation.
- **Feature Overlap:** Rather than fully integrating the datasets, the analysis focused on comparing and contrasting similar features to uncover broader patterns and relationships.

## Artifacts in GitHub Repository
The following artifacts are available in the project’s GitHub repository:

- `data_acquisition.ipynb`: Data loading and initial inspection
- `data_cleaning_preprocessing.ipynb`: Data cleaning and preprocessing steps
- `eda_visualizations.ipynb`: Exploratory data analysis, including visualizations and key insights
- `model_dev_baseline.ipynb`: Model development and evaluation using standard machine learning practices
- `requirements.txt`: List of Python dependencies for reproducibility

## Next Steps
The project is approaching its final stages, with the following tasks scheduled for completion:

- **Final Model Tuning:** Further refinement of the predictive model using cross-validation and GridSearch to optimize hyperparameters.
- **Feature Importance Analysis:** Incorporate advanced techniques such as SHAP values to interpret model predictions and identify the most influential features.
- **Final Report Drafting:** Begin drafting the final project report, summarizing methodology, findings, and implications.
- **Workflow Packaging:** Prepare and upload all results and outputs to Box for final submission.
- **Archiving:** Archive the project on Zenodo and finalize metadata for long-term preservation. 
- **README.md:** Project overview, structure, and setup instructions

---

**Status Report Prepared by:** Shivali Patel

**GitHub Repository:** illinois-data-curation/is477-sp25-group39

---

This comprehensive status report reflects significant progress toward understanding the intersection between academic performance and mental health among students. The project’s structured approach, attention to detail, and adaptability in the face of data integration challenges have laid a strong foundation for impactful findings and actionable insights. As the project moves into its final phase, emphasis will be placed on refining the predictive model, deepening the interpretability of results, and ensuring that all documentation and artifacts are complete and accessible for future reference and application.