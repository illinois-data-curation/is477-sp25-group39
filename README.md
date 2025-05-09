# Mental Health and Academic Performance Analysis

## Link to Archival Record
[Zenodo DOI Placeholder – To be updated after GitHub release and Zenodo upload]

## 👥 Contributors
- **Shivali Patel**  
  *Undergraduate Student, University of Illinois at Urbana-Champaign*

---

## Summary

This project explores the growing concern surrounding mental health in academic environments, specifically the prevalence and impact of depression among college students. The main motivation behind this work stems from widespread evidence that depression among students is not only underdiagnosed but often overlooked by academic institutions until academic performance begins to decline. As educational institutions continue to adopt data-driven interventions to support students’ academic and personal wellbeing, this study aims to examine whether early signs of depression can be identified through academic, lifestyle, and behavioral indicators.

Our goal is to understand what factors most strongly predict depression and to build a predictive model capable of identifying students who may be at risk. The following research questions guided the development of this project:

1. What academic and behavioral variables are most strongly associated with depression?
2. Can academic performance alone predict whether a student is likely to experience depression?
3. How do lifestyle-related features such as sleep patterns, stress levels, and study duration interact with depression risk?
4. What impact do external pressures like financial stress and family history of mental illness have on student mental health?

To answer these questions, we analyzed two datasets obtained from Kaggle. The first dataset focused on mental health factors, while the second was centered on academic performance. Data wrangling included cleaning null values, encoding categorical features, and transforming one dataset from JSON to CSV format for easier integration. The analysis pipeline included exploratory data analysis (EDA), statistical visualization, and predictive modeling using machine learning classifiers like Random Forest and Logistic Regression.

The results showed that the depression dataset produced a high-performing model with an AUC of 0.91, indicating that behavioral and lifestyle indicators were strong predictors. Conversely, academic performance data alone failed to provide meaningful prediction accuracy (AUC = 0.51). These findings support the hypothesis that while academic indicators contribute to understanding depression risk, it is the combination of lifestyle and stress-related variables that offer stronger predictive power.

In summary, the study underscores the potential of predictive modeling as a tool for early intervention. By identifying students at risk of depression using non-invasive, institutionally available data, academic institutions can deploy wellness resources more effectively and proactively.

---

## Data Profile

### Dataset 1: Student Depression Dataset
- **Source**: Kaggle  
- **License**: Creative Commons Attribution 4.0 (CC BY 4.0)  
- **URL**: https://www.kaggle.com/datasets/adilshamim8/student-depression-dataset  
- **Format**: CSV  

This dataset contains survey responses from students regarding academic stress, mental well-being, and overall lifestyle. It includes fields such as:
- CGPA
- Academic pressure and satisfaction
- Sleep duration and study habits
- Financial stress levels
- Depression diagnosis (binary: 0/1)
- Family history of mental illness

The depression variable served as the target for classification. One of the primary challenges with this dataset was the presence of missing values and categorical variables that needed to be one-hot encoded. For example, sleep duration was originally formatted as text ("5-6 hours") and required transformation into numeric values. Furthermore, while CGPA was already numeric, it required normalization to support model convergence.

Another key challenge was the imbalance in depression class distribution. Although not extreme, a larger portion of students in the dataset did not report depression, requiring the use of stratified sampling to ensure reliable model training and evaluation.

---

### Dataset 2: Student Grading & Behavior Dataset
- **Source**: Kaggle  
- **License**: CC0 1.0 Universal (Public Domain)  
- **URL**: https://www.kaggle.com/datasets/mahmoudelhemaly/students-grading-dataset  
- **Format**: JSON (converted to CSV)

This dataset includes data about student academic performance, stress levels, and basic demographic and family background indicators. Some of the fields included:
- Attendance percentage
- Midterm and final scores
- Average assignment and quiz performance
- Participation and project scores
- Reported stress level (scale 1–10)
- Sleep hours per night
- Parent education level and family income level

Unlike the first dataset, this one was not directly labeled with depression or mental health status. Therefore, the project used a proxy classification task, where we labeled students as either passing or failing based on final grades. This binary target variable (`pass_fail`) was generated by mapping letter grades to numeric scores and setting a threshold at 60%.

A significant issue with this dataset was that the JSON structure required flattening and normalization. Many records had missing or placeholder values, which we addressed through median imputation or dropping irrelevant fields. Overall, this dataset proved more challenging to model effectively due to the lack of a mental health-specific target and the relatively weak correlation between academic metrics and performance outcomes.

---

## Findings

### Depression Dataset (Classification Task: Depression = 1 or 0)
- **Best Parameters**: `n_estimators=200`, `max_depth=20`, `min_samples_split=5`
- **Accuracy**: 84%
- **ROC AUC Score**: **0.91**
- **F1 Score for Depression Class**: 0.87
- **Confusion Matrix**:
  ```
  [[1783  530]
   [ 372 2896]]
  ```

The Random Forest model trained on the cleaned depression dataset performed very well. CGPA, academic pressure, financial stress, and job satisfaction were among the top features. Visualizations revealed that students with higher academic pressure and financial strain were more likely to experience depression, as supported by correlation heatmaps. Boxplots comparing CGPA to depression status showed only subtle variation, suggesting GPA alone isn’t a strong depression indicator.

---

### Academic Performance Dataset (Classification Task: Pass vs. Fail)
- **Best Parameters**: `n_estimators=200`, `max_depth=10`, `min_samples_split=5`
- **Accuracy**: 78%
- **ROC AUC Score**: **0.51**
- **F1 Score (Failing Class)**: 0.04
- **Confusion Matrix**:
  ```
  [[  4 197]
   [ 20 779]]
  ```

Performance modeling did not produce reliable results. Most features like test scores and participation had low correlation with the target, and the class imbalance severely impacted recall and precision in the failing class. Heatmaps and ROC curves confirmed that the model barely performed better than random guessing. This affirmed our hypothesis that academic metrics alone are not enough to predict meaningful student risk categories.

---

## Future Work

### Lessons Learned:
This project taught several key lessons:
- High-quality data is crucial. Without shared identifiers or labels, integration and joint analysis are limited.
- Preprocessing—especially one-hot encoding and normalization—has a large impact on model performance.
- Predictive models require careful attention to bias, class imbalance, and ethical interpretation, especially in mental health contexts.

### Future Directions:
In a future version of this project, we would:
- Add model interpretability tools like SHAP to better understand feature impact
- Collect or simulate temporal data to study mental health trends over time
- Expand the dataset by combining institutional data like attendance logs, help-desk visits, or counseling appointments
- Partner with student support departments to evaluate real-world deployment as a risk-assessment tool

---

## Reproducing the Project

To reproduce this project:

1. Clone the GitHub repository:
   ```bash
   git clone https://github.com/illinois-data-curation/is477-sp25-group39.git
   cd is477-sp25-group39
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Execute the full pipeline:
   ```bash
   python run_all.py
   ```

### Data Access & Folder Structure

All cleaned output data, visualizations, and results have been uploaded to Box.

[Box Folder – Project Output Files](https://uofi.box.com/s/egvyn48ba590yclftzowf6hnu0r7vhi8)

Please download and extract the contents into the `/data/` folder in the project root.

Note: The `/data/` folder has been added to `.gitignore` to prevent large files from being committed to GitHub.

---

## References

- Adil Shamim. *Student Depression Dataset*. Kaggle. https://www.kaggle.com/datasets/adilshamim8/student-depression-dataset  
- Mahmoud Elhemaly. *Student Grading Dataset*. Kaggle. https://www.kaggle.com/datasets/mahmoudelhemaly/students-grading-dataset  
- Scikit-learn: https://scikit-learn.org  
- Seaborn: https://seaborn.pydata.org  
- Matplotlib: https://matplotlib.org  
