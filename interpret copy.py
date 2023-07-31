import json

def filter_results(data):
    sentence_results = []
    
    for sentence in data['sentences']:
        for result in sentence['result']:
            if result['etype'] != 'no_error':
                sentence_result = {}
                sentence_result['input'] = result['input']
                sentence_result['output'] = result['output']
                sentence_result['etype'] = result['etype']
                # Use dict.get() method with a default value
                sentence_result['help'] = result.get('help', 'No help available')
                sentence_results.append(sentence_result)
                
    # Save the results in a JSON file
    with open('filtered_results.json', 'w') as json_file:
        json.dump(sentence_results, json_file)

# Load the data from the JSON file
with open('results.json') as f:
    data = json.load(f)

# Call the function with our data
filter_results(data)
