import subprocess
import json

# Run extract.py and capture the output
result = subprocess.run(['python3', 'extract.py'], stdout=subprocess.PIPE, text=True)

# The stdout property contains the output
input_text = result.stdout.strip()  # Use strip to remove trailing newline

# Prepare the data for the curl command
data = {
    "query": input_text,  # Use the output of extract.py
    "help": "on"
}

# Convert the data to a JSON string
data_str = json.dumps(data)

# Prepare the curl command
curl_command = [
    "curl", "-v", "-X", "POST", {"KAKAO_ENDPOINT_URL"},
    "-H", "x-api-key: {KAKAO_API_KEY }",
    "-H", "Content-Type: application/json",
    "-d", data_str  # Pass the data to the curl command
]

# Run the curl command
process_b = subprocess.run(curl_command, text=True, capture_output=True)

# Write the output to a file
with open('results.json', 'w') as f:
    f.write(process_b.stdout)
