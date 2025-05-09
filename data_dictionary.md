# Data Dictionary 

## Student Depression Dataset

| Variable Name                              | Description                                                  | Type        | Example Values                     | Notes                                         |
|-------------------------------------------|--------------------------------------------------------------|-------------|------------------------------------|-----------------------------------------------|
| `id`                                       | Unique identifier for each student                           | Integer     | 2, 8, 26                           | Should not be used as a feature               |
| `gender`                                   | Gender of the student                                        | Categorical | Male, Female                       | May need encoding                            |
| `age`                                      | Age of the student                                           | Numeric     | 24, 28, 33                         | Range varies from early 20s to 30s            |
| `city`                                     | Student's city of residence                                  | Categorical | Bangalore, Jaipur                  | May not be useful for modeling unless grouped |
| `profession`                               | Student's occupation                                         | Categorical | Student                            | Mostly constant                               |
| `academic_pressure`                        | Level of academic pressure (scale)                           | Ordinal     | 1.0–5.0                            | Higher means more pressure                    |
| `work_pressure`                            | Level of work pressure (scale)                               | Ordinal     | 0.0–5.0                            | Mostly 0 for students                         |
| `cgpa`                                     | Cumulative Grade Point Average                               | Numeric     | 5.59, 8.13                         | Scale of 0–10                                 |
| `study_satisfaction`                       | Satisfaction with study experience                           | Ordinal     | 1.0–5.0                            | Higher is more satisfied                      |
| `job_satisfaction`                         | Satisfaction with work/study situation                       | Ordinal     | 0.0–5.0                            | Low variation in students                     |
| `sleep_duration`                           | Reported sleep per night                                     | Categorical | 'Less than 5 hours', '5-6 hours'   | Convert to numeric (e.g., 4.5, 5.5, etc.)      |
| `dietary_habits`                           | Type of dietary habits                                       | Categorical | Healthy, Moderate                  | Could be ordinal if ranked                    |
| `degree`                                   | Degree pursued                                               | Categorical | BCA, M.Tech, B.Pharm               | One-hot encoding suggested                    |
| `have_you_ever_had_suicidal_thoughts_?`    | Suicidal ideation history                                    | Binary      | Yes, No                            | Sensitive – use ethically                     |
| `work/study_hours`                         | Average hours per day dedicated to work/study                | Numeric     | 1.0–9.0                            | Continuous variable                           |
| `financial_stress`                         | Financial stress score                                       | Ordinal     | 1.0–5.0                            | Higher = more stressed                        |
| `family_history_of_mental_illness`         | Whether there's family history of mental illness             | Binary      | Yes, No                            | May be predictive                             |
| `depression`                               | Depression status (target variable)                          | Binary      | 1 (Yes), 0 (No)                    | Target variable for classification            |



## Student Performance & Behavior Dataset

| Variable Name                   | Description                                          | Type        | Example Values                    | Notes                                        |
|--------------------------------|------------------------------------------------------|-------------|-----------------------------------|----------------------------------------------|
| `student_id`                   | Unique identifier for each student                  | Integer     | 1001, 1042                        | Ignore during modeling                       |
| `first_name`, `last_name`      | Names of student                                    | Text        | N/A                               | Drop or anonymize                            |
| `email`                        | Email address                                       | Text        | N/A                               | Drop for privacy                             |
| `gender`                       | Gender of the student                               | Categorical | Male, Female                      | Already encoded in some cases                |
| `age`                          | Student age                                         | Numeric     | 19–24                             |                                               |
| `department`                   | Student's department/major                          | Categorical | Engineering, Arts, etc.           | Use one-hot or group                         |
| `attendance_(%)`               | Attendance rate as percentage                       | Numeric     | 75, 88, 95                        | Can normalize                                |
| `midterm_score`                | Score on midterm exam                               | Numeric     | 45–100                            | Continuous                                   |
| `final_score`                  | Score on final exam                                 | Numeric     | 50–100                            | Continuous                                   |
| `assignments_avg`             | Average score across assignments                    | Numeric     | 60–95                             | Continuous                                   |
| `quizzes_avg`                 | Average score across quizzes                        | Numeric     | 55–100                            | Continuous                                   |
| `participation_score`         | Score for participation in class                    | Numeric     | 0–100                             |                                              |
| `projects_score`              | Project score                                        | Numeric     | 50–100                            |                                              |
| `total_score`                 | Aggregated score across all categories              | Numeric     | 60–100                            |                                              |
| `grade`                       | Letter or numeric grade                             | Categorical | A, B, C, D, F or 90, 80, etc.     | Use consistent format                        |
| `study_hours_per_week`        | Weekly study hours                                  | Numeric     | 5–40                              | May have outliers                            |
| `extracurricular_activities`  | Whether the student participates in extracurriculars| Binary      | Yes, No                           |                                              |
| `internet_access_at_home`     | Whether the student has internet access at home     | Binary      | Yes, No                           |                                              |
| `parent_education_level`      | Education level of student's parents                | Categorical | High School, PhD, Bachelor's      | One-hot or ordinal encoding                  |
| `family_income_level`         | Household income level                              | Ordinal     | Low, Medium, High                 | Encode as ordinal                            |
| `stress_level_(1-10)`         | Self-reported stress level                          | Ordinal     | 1–10                              | Higher = more stress                         |
| `sleep_hours_per_night`       | Average sleep hours per night                       | Numeric     | 4–9                               | Can be binned                                |
