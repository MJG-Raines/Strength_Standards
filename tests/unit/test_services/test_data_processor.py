from src.services.data_processor import analyze_powerlifting_data

def test_analyze_powerlifting_data():
    # Arrange - set up test data
    sex = 'M'
    age = 50
    bodyweight = 270

    # Act - call the function
    results = analyze_powerlifting_data(sex, age, bodyweight)

    # Assert - verify the results
    assert isinstance(results, dict), "Results should be a dictionary"
    assert 'all_time' in results, "Should have all_time key"
    assert 'current_year' in results, "Should have current_year key"
    
    # For pandas DataFrame/Series
    assert len(results['all_time'].index) == 50, "Should have 50 all-time entries"
    assert len(results['current_year'].index) == 10, "Should have 10 current year entries"

    # Check for expected columns
    expected_columns = ['Name', 'BenchLBS', 'BodyweightLBS', 'Date']
    assert all(col in results['all_time'].columns for col in expected_columns), "Missing expected columns"