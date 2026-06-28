import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

def calculate_bmi(weight: float, height_cm: float) -> float:
    height_m = height_cm / 100
    return float(np.round(weight / np.power(height_m, 2), 2))

def get_fitness_score(bmi: float, pushups: int, run_time: float, sleep: float, 
                      water: float, smoking: str, alcohol: int) -> int:
    score = 100

    if bmi < 18.5: score -= 10
    elif 18.5 <= bmi <= 24.9: score += 0
    elif 25 <= bmi <= 29.9: score -= 10
    else: score -= 20

    if pushups >= 50: score += 10
    elif pushups >= 30: score += 5
    elif pushups >= 15: score += 0
    else: score -= 10

    if run_time <= 4.5: score += 10
    elif run_time <= 6.0: score += 5
    elif run_time <= 8.0: score += 0
    else: score -= 10

    if sleep >= 8: score += 5
    elif sleep >= 7: score += 0
    elif sleep < 6: score -= 10

    if water >= 2.5: score += 5
    elif water < 1.5: score -= 5

    if smoking == 'Y': score -= 15
    
    if alcohol == 0: score += 5
    elif alcohol > 5: score -= 10

    return max(0, min(100, score))

def get_category(score: int) -> str:
    if score >= 90: return "Elite"
    if score >= 75: return "Above Average"
    if score >= 60: return "Average"
    return "Needs Improvement"

def display_pandas_summary(data_dict: dict):
    print("\n" + "=" * 60)
    print("                PANDAS DATA SUMMARY")
    print("=" * 60)
    
    df = pd.DataFrame(list(data_dict.items()), columns=['Metric', 'Value'])
    df['Value'] = df['Value'].apply(lambda x: f"{x:.2f}" if isinstance(x, float) else x)
    
    print(df.to_string(index=False))
    print("=" * 60)

def plot_comprehensive_dashboard(data: dict):
    fig, axs = plt.subplots(1, 3, figsize=(15, 5))
    fig.suptitle(f"Fitness Dashboard: {data['Name']} (Category: {data['Category']})", fontsize=16, fontweight='bold')

    axs[0].bar(["Actual Age", "Fitness Age"], [data['Actual Age'], data['Fitness Age']], color=['#7f7f7f', '#17becf'])
    axs[0].set_title("Age Comparison")
    axs[0].set_ylabel("Years")
    axs[0].grid(axis='y', linestyle='--', alpha=0.7)

    physical_keys = ['BMI', 'Pushups', 'Run Time (min)']
    physical_vals = [data['BMI'], data['Pushups'], data['Run Time (min)']]
    axs[1].bar(physical_keys, physical_vals, color=['#1f77b4', '#ff7f0e', '#2ca02c'])
    axs[1].set_title("Physical Metrics")
    axs[1].grid(axis='y', linestyle='--', alpha=0.7)

    axs[2].barh(["Fitness Score"], [data['Score']], color='#d62728')
    axs[2].set_xlim(0, 100)
    axs[2].set_title("Overall Fitness Score (out of 100)")
    axs[2].grid(axis='x', linestyle='--', alpha=0.7)

    plt.tight_layout()
    plt.show()

def main():
    print("=" * 60)
    print("           AI FITNESS AGE CALCULATOR v2.0")
    print("=" * 60)

    name = input("Enter your name: ")
    gender = input("Enter your gender (M/F): ").strip().upper()
    age = int(input("Enter your age: "))
    height = float(input("Enter your height (cm): "))
    weight = float(input("Enter your weight (kg): "))
    
    pushups = int(input("Maximum pushups in one set: "))
    run_time = float(input("1 km run time (minutes): "))
    
    sleep = float(input("Average sleep per day (hours): "))
    water = float(input("Daily water intake (liters): "))
    smoking = input("Do you smoke? (Y/N): ").strip().upper()
    alcohol = int(input("Alcoholic drinks per week (0 if none): "))

    bmi = calculate_bmi(weight, height)
    score = get_fitness_score(bmi, pushups, run_time, sleep, water, smoking, alcohol)
    fitness_age = round(age + ((100 - score) / 4), 1)
    category = get_category(score)

    user_record = {
        "Name": name,
        "Gender": gender,
        "Actual Age": age,
        "Fitness Age": fitness_age,
        "BMI": bmi,
        "Pushups": pushups,
        "Run Time (min)": run_time,
        "Sleep (hrs)": sleep,
        "Water (L)": water,
        "Smoking Status": "Yes" if smoking == 'Y' else "No",
        "Alcohol (drinks/wk)": alcohol,
        "Score": score,
        "Category": category
    }

    display_pandas_summary(user_record)

    print("\n[AI Insights]")
    if fitness_age < age:
        print("-> Excellent! Your fitness age is younger than your actual age.")
    elif fitness_age == age:
        print("-> Your fitness age matches your actual age.")
    else:
        print("-> Improving physical activity and lifestyle habits could lower your fitness age.")

    print("\nGenerating visual dashboard...")
    plot_comprehensive_dashboard(user_record)

if '__name__' == "_main_":
    main()