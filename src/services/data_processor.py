import pandas as pd
from datetime import datetime

def analyze_powerlifting_data(sex: str, age: int, bodyweight: float):
    """
    Main function to process data based on user input.
    All weights should be in pounds.
    """
    file_path = '/Users/TMJ/Strength_Standards/src/data/raw/openpowerlifting-2025-02-08-94006796.csv'
    
    # Read data - adding Equipment column
    df = pd.read_csv(file_path, usecols=['Name', 'Sex', 'Age', 'BodyweightKg', 'Best3BenchKg', 'Date', 'Equipment'])
    
    # Initial cleanup and conversion
    bench_data = df[df['Best3BenchKg'].notna()].copy()
    bench_data['BenchLBS'] = bench_data['Best3BenchKg'] * 2.20462
    bench_data['BodyweightLBS'] = bench_data['BodyweightKg'] * 2.20462
    
    # Filter for raw life lifts only
    bench_data = bench_data[bench_data['Equipment'] == 'Raw']

    # Remove duplicates based on Name and Date (keeping highest bench for that day)
    bench_data = bench_data.sort_values('BenchLBS', ascending=False).drop_duplicates(subset=['Name', 'Date'], keep='first')
    
    # Filter by sex
    filtered_data = bench_data[bench_data['Sex'] == sex]
    
    # Filter by age group
    if 20 <= age <= 23:
        filtered_data = filtered_data[(filtered_data['Age'] >= 20) & (filtered_data['Age'] <= 23)]
    elif 24 <= age <= 34:
        filtered_data = filtered_data[(filtered_data['Age'] >= 24) & (filtered_data['Age'] <= 34)]
    elif 35 <= age <= 39:
        filtered_data = filtered_data[(filtered_data['Age'] >= 35) & (filtered_data['Age'] <= 39)]
    elif 40 <= age <= 44:
        filtered_data = filtered_data[(filtered_data['Age'] >= 40) & (filtered_data['Age'] <= 44)]
    elif 45 <= age <= 49:
        filtered_data = filtered_data[(filtered_data['Age'] >= 45) & (filtered_data['Age'] <= 49)]
    elif 50 <= age <= 54:
        filtered_data = filtered_data[(filtered_data['Age'] >= 50) & (filtered_data['Age'] <= 54)]
    elif 55 <= age <= 59:
        filtered_data = filtered_data[(filtered_data['Age'] >= 55) & (filtered_data['Age'] <= 59)]
    elif 60 <= age <= 64:
        filtered_data = filtered_data[(filtered_data['Age'] >= 60) & (filtered_data['Age'] <= 64)]
    elif 65 <= age <= 69:
        filtered_data = filtered_data[(filtered_data['Age'] >= 65) & (filtered_data['Age'] <= 69)]
    elif 70 <= age <= 74:
        filtered_data = filtered_data[(filtered_data['Age'] >= 70) & (filtered_data['Age'] <= 74)]
    elif age >= 75:
        filtered_data = filtered_data[filtered_data['Age'] >= 75]

    # Filter by weight class
    if sex == 'M':
        if bodyweight <= 114:
            filtered_data = filtered_data[filtered_data['BodyweightLBS'] <= 114]
        elif bodyweight <= 123:
            filtered_data = filtered_data[filtered_data['BodyweightLBS'] <= 123]
        elif bodyweight <= 132:
            filtered_data = filtered_data[filtered_data['BodyweightLBS'] <= 132]
        elif bodyweight <= 148:
            filtered_data = filtered_data[filtered_data['BodyweightLBS'] <= 148]
        elif bodyweight <= 165:
            filtered_data = filtered_data[filtered_data['BodyweightLBS'] <= 165]
        elif bodyweight <= 181:
            filtered_data = filtered_data[filtered_data['BodyweightLBS'] <= 181]
        elif bodyweight <= 198:
            filtered_data = filtered_data[filtered_data['BodyweightLBS'] <= 198]
        elif bodyweight <= 220:
            filtered_data = filtered_data[filtered_data['BodyweightLBS'] <= 220]
        elif bodyweight <= 242:
            filtered_data = filtered_data[filtered_data['BodyweightLBS'] <= 242]
        elif bodyweight <= 275:
            filtered_data = filtered_data[filtered_data['BodyweightLBS'] <= 275]
        elif bodyweight <= 308:
            filtered_data = filtered_data[filtered_data['BodyweightLBS'] <= 308]
        else:
            filtered_data = filtered_data[filtered_data['BodyweightLBS'] > 308]
    else:  # Female
        if bodyweight <= 97:
            filtered_data = filtered_data[filtered_data['BodyweightLBS'] <= 97]
        elif bodyweight <= 105:
            filtered_data = filtered_data[filtered_data['BodyweightLBS'] <= 105]
        elif bodyweight <= 114:
            filtered_data = filtered_data[filtered_data['BodyweightLBS'] <= 114]
        elif bodyweight <= 123:
            filtered_data = filtered_data[filtered_data['BodyweightLBS'] <= 123]
        elif bodyweight <= 132:
            filtered_data = filtered_data[filtered_data['BodyweightLBS'] <= 132]
        elif bodyweight <= 148:
            filtered_data = filtered_data[filtered_data['BodyweightLBS'] <= 148]
        elif bodyweight <= 165:
            filtered_data = filtered_data[filtered_data['BodyweightLBS'] <= 165]
        elif bodyweight <= 181:
            filtered_data = filtered_data[filtered_data['BodyweightLBS'] <= 181]
        elif bodyweight <= 198:
            filtered_data = filtered_data[filtered_data['BodyweightLBS'] <= 198]
        else:
            filtered_data = filtered_data[filtered_data['BodyweightLBS'] > 198]

    # Get results
    # Format output to round numbers nicely
    all_time = filtered_data.nlargest(50, 'BenchLBS')[['Name', 'BenchLBS', 'BodyweightLBS', 'Date']]
    all_time['BenchLBS'] = all_time['BenchLBS'].round(2)
    all_time['BodyweightLBS'] = all_time['BodyweightLBS'].round(2)
    
    # Current year
    current_year = str(datetime.now().year)
    current_year_data = filtered_data[filtered_data['Date'].str[:4] == current_year]
    current_year_top = current_year_data.nlargest(10, 'BenchLBS')[['Name', 'BenchLBS', 'BodyweightLBS', 'Date']]
    current_year_top['BenchLBS'] = current_year_top['BenchLBS'].round(2)
    current_year_top['BodyweightLBS'] = current_year_top['BodyweightLBS'].round(2)
    
    return {
        'all_time': all_time,
        'current_year': current_year_top
    }