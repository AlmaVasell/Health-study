from analysis.stats_functions import summary_statistics
from analysis.plotting import bp_histogram, bp_vs_age
from analysis.health_analyzer import HealthAnalyzer
import pandas as pd

df = pd.read_csv("health_study_dataset.csv")

stats = summary_statistics(df, ["age", "weight", "height", "systolic_bp", "cholesterol"])
print(stats)

bp_histogram(df)
bp_vs_age(df)

analyzer = HealthAnalyzer(df)
print("Medel blodtryck:", analyzer.mean_bp())

model = analyzer.regression_age_weight()
print("Regressionskoefficienter:", model.coef_)
