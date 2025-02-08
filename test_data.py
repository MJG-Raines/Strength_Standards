from src.services.data_processor import analyze_powerlifting_data

# Test with example inputs
results = analyze_powerlifting_data(
    sex='M',      # 'M' for male, 'F' for female
    age=50,       # Any age
    bodyweight=270 # Any weight in pounds
)

print("\nTop 25 All-Time:")
print(results['all_time'])
print("\nTop 10 Current Year:")
print(results['current_year'])