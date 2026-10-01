# CodeAlpha Task 2 — Exploratory Data Analysis (EDA)

## Student Performance Dataset

### Project Overview

This project was completed as part of the **CodeAlpha Data Analytics Internship — Task 2: Exploratory Data Analysis (EDA)**.

The objective of this project is to explore a student performance dataset, understand its structure, identify meaningful patterns and trends, detect potential anomalies, and investigate relationships between student characteristics and academic performance using statistical analysis and visualization.

---

## Dataset

The project uses the **Student Performance Dataset** from the UCI Machine Learning Repository.

The dataset contains information about students, including:

- Demographic information
- Family and social characteristics
- Study habits
- Previous academic failures
- Absences
- Previous-period grades
- Final grade

### Dataset Dimensions

- **Rows:** 649
- **Columns:** 33

### Target Variable

`G3` — Final student grade.

---

## Technologies and Libraries

- Python
- Jupyter Notebook
- Pandas
- NumPy
- Matplotlib
- Seaborn
- SciPy
- UCI ML Repository (`ucimlrepo`)

---

## EDA Process

The analysis followed these major steps:

1. Loaded and inspected the dataset
2. Examined dataset structure and data types
3. Checked for missing values and duplicate records
4. Performed descriptive statistical analysis
5. Analyzed the distribution of final grades
6. Investigated study time and final grades
7. Performed one-way ANOVA
8. Performed Tukey HSD post-hoc analysis
9. Investigated absences and final grades
10. Performed Pearson correlation testing
11. Analyzed previous academic failures and final grades
12. Created a numerical-variable correlation heatmap
13. Detected potential outliers using the IQR method
14. Summarized the findings and data-quality observations

---

## Key Findings

### Final Grade Distribution

The final grade (`G3`) ranges from **0 to 19**.

- Mean: approximately **11.91**
- Median: **12**
- Standard deviation: approximately **3.23**

### Study Time and Final Grade

Students in higher study-time categories generally had higher average final grades.

A one-way ANOVA produced:

- F-statistic: **15.8763**
- p-value: approximately **5.71 × 10⁻¹⁰**

The result provides statistical evidence that mean final grades differ across some study-time categories.

Tukey HSD was subsequently used to identify which study-time groups differed significantly.

### Absences and Final Grade

The Pearson correlation between absences and final grade was approximately:

**-0.0914**

with a p-value of approximately:

**0.0199**

This indicates a statistically significant but **very weak negative linear association** between absences and final grades.

### Previous Failures and Final Grade

Students with no previous academic failures had an average final grade of approximately **12.51**.

Students with one or more previous failures had lower average final grades in this dataset.

The groups with two and three previous failures were relatively small, so their results should be interpreted cautiously.

### Outlier Detection

Using the IQR method for absences:

- Q1: **0**
- Q3: **6**
- IQR: **6**
- Upper bound: **15**
- Potential high-end outliers: **21 students**

These observations are not automatically considered errors because they may represent genuine high absenteeism.

---

## Data Quality

The dataset was checked for common data-quality issues.

- Missing values: **0**
- Duplicate rows: **0**
- Potential high-end absence outliers: **21**

The analysis also identified small sample sizes in some categories, which should be considered when interpreting group-level statistics.

---

## Visualizations

The project includes visualizations such as:

- Final grade distribution
- Final grade boxplot
- Average final grade by study time
- Final grade distribution by study time
- Absence distribution
- Absences vs. final grade scatter plot
- Final grade by previous academic failures
- Numerical-variable correlation heatmap

The generated visualization files are stored in the `screenshots` folder.

---

## Project Structure

```text
CodeAlpha_EDA/
│
├── data/
│   └── student_performance.csv
│
├── notebooks/
│   └── CodeAlpha_EDA_Analysis.ipynb
│
├── screenshots/
│   ├── g3_distribution.png
│   ├── g3_boxplot.png
│   ├── studytime_vs_g3.png
│   ├── studytime_g3_boxplot.png
│   ├── absences_distribution.png
│   ├── absences_vs_g3.png
│   ├── failures_vs_g3.png
│   └── correlation_heatmap.png
│
├── src/
│   └── download_dataset.py
│
├── requirements.txt
└── README.md
```

---

## Statistical Methods Used

The project uses several statistical techniques:

- Descriptive statistics
- Pearson correlation
- Pearson correlation significance test
- One-way ANOVA
- Tukey HSD post-hoc test
- IQR-based outlier detection

These methods were used to investigate relationships and differences within the dataset.

---

## Important Interpretation Note

This analysis is based on observational student data. Statistical associations identified during the EDA should **not be interpreted as proof of causation**.

For example, the observed relationship between study time and final grades does not by itself prove that increasing study time directly causes higher grades.

---

## Conclusion

The exploratory analysis provided an understanding of the structure, quality, distributions, relationships, and potential anomalies in the Student Performance Dataset.

The analysis identified meaningful associations involving study time, previous academic failures, absences, and final grades. Statistical testing and visualization were used to support these observations.

The dataset contains no missing values or duplicate rows, while unusually high absence values and small subgroup sizes represent areas that should be considered in further analysis.

This EDA provides a foundation for future statistical analysis or predictive modeling using the student performance data.
