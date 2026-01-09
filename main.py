import json
from agent import analyze_requirements

with open("sample_input.json", "r") as file:
    data = json.load(file)

user_story = data["user_story"]

result = analyze_requirements(user_story)

with open("sample_output.json", "w") as file:
    json.dump(result, file, indent=4)

print("Done! sample_output.json is created.")
