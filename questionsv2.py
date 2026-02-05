"""
Questionare for WMC26
"""
def get_choice(prompt, options):
    """Helper to ensure the user picks a valid option."""
    while True:
        formatted_options = "/".join(options)
        user_input = input(f"{prompt} ({formatted_options}): ").strip().lower()
        # Find the actual option that matches the input
        for opt in options:
            if user_input == opt.lower():
                return opt
        print(f"--- Invalid input. Please choose from: {formatted_options} ---")

print("="*40)
print("   SOFTWARE SECURITY & QUALITY SURVEY   ")
print("="*40)

results = {}

# Logic Flow
usage = get_choice("Do you use QA/SAST tools?", ["Yes", "No"])
results['uses_tools'] = 

if usage == "Yes":
    results['context'] = get_choice("What for?", ["Work", "Personal Projects", "Both"])

    problem_solve = get_choice("What problems do they solve?", 
                    ["Vulnerabilities", "Code Quality", "Both", "None"])
    results['benefit'] = problem_solve

    if problem_solve == "None":
        results['reason_why_none'] = get_choice("Why not?", 
            ["Too complex", "Not useful", "Too much noise", "Unsure"])
    else:
        results['frequency'] = get_choice("How often?", 
            ["Always", "Often", "Sometimes", "Rarely"])

else:
    results['barrier'] = get_choice("Why not?", 
        ["Unknown", "Lack of trust", "Expensive", "Noise"])
    results['future_use'] = get_choice("Would you consider them later?", ["Yes", "No"])

# Final Rating
while True:
    try:
        rating = int(input("How do you evaluate them from 1-10? "))
        if 1 <= rating <= 10:
            results['rating'] = rating
            break
    except ValueError:
        pass
    print("--- Please enter a number between 1 and 10 ---")

print("\n" + "-"*40)
print("Submission successful. Thank you for your participation!")
print("-"*40)
