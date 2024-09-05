# Insurance Cost Prediction Project
## Deployed Application
You can access the deployed web application here: (https://cost-prediction.streamlit.app/)
## Problem Statement
Insurance companies need accurate health insurance cost predictions for setting appropriate premiums. 
Traditional methods often fall short in accounting for individual differences. Leveraging machine learning can improve prediction accuracy,
competitive pricing, and risk management.

## Project Need
### Objectives:
- **Precision in Pricing**: Use individual data points for accurate risk-based premiums.
- **Competitiveness**: Offer attractive and sustainable rates.
- **Customer Satisfaction**: Ensure fair, transparent pricing.
- **Personalized Offerings**: Tailor insurance packages to individual needs.
- **Risk Assessment**: Refine risk assessment processes.
- **Policy Development**: Inform new product development.
- **Strategic Decision Making**: Aid in market entry and policy adjustments.
- **Customer Engagement**: Use insights for personalized marketing and advice.

## Data Description
The dataset includes:
- Age, Diabetes, BloodPressureProblems, AnyTransplants, AnyChronicDiseases, Height, Weight, KnownAllergies,
- HistoryOfCancerInFamily, NumberOfMajorSurgeries, PremiumPrice.

## Block 1: Tableau Visualization
  Goals:
- **Visualize Key Data Points**: Show distribution and impact of health factors on premiums.
- **Predictive Analysis**: Predict costs based on risk factors.
- **Strategic Insights**: Derive insights for policy adjustments and risk assessments

## Block 2: EDA and Hypothesis Testing
### Goals:
Understand predictors of insurance costs through visualizations and statistical tests.

### Ideas:
- **Distribution Analysis**: Various visualizations.
- **Correlation Analysis**: Correlation matrix/heatmap.
- **Outlier Detection**: IQR or Z-scores.
- **Hypothesis Testing**: T-tests, ANOVA, Chi-square tests, regression analysis.

## Block 3: ML Modeling
### Steps:
1. **Data Preprocessing**: Handle missing values, feature engineering, scaling, encoding.
2. **Model Selection**: Linear regression, tree-based models, neural networks.
3. **Evaluation and Validation**: Cross-validation, RMSE, MAE, R².
4. **Interpretability**: Feature importance, actionable insights.

## Results 
### Model : RandomforestRegressor 
### R² : 0.90


## Block 4: Web-Based Calculator
### Goal:
Deploy a user-friendly web application for real-time insurance premium predictions.

### Deployment:
- **Streamlit App**: User interface for input forms and real-time predictions.

---

