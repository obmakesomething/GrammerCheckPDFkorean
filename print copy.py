import json

# Load the data from the JSON file
with open('filtered_results.json', 'r') as f:
    filtered_results = json.load(f)

# Convert the filtered results to a readable format
readable_results = []
for result in filtered_results:
    readable_result = f"""
    원래 텍스트: {result['input']}
    수정된 텍스트: {result['output']}
    오류 유형: {result['etype']}
    도움말: {' '.join(result['help'])}
    """
    readable_results.append(readable_result)

# Print all the readable results
print('\n'.join(readable_results))
