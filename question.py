"""
Questionare for WMC26
"""
def run_survey():
    print("--- Software Quality & Security Tooling Survey ---")

    # 1. Discovery Source
    discovery_source = input("How do you typically discover QA/SAST tools?\"
    "\n(Individual research, Trusted peer, Advertisements): ").strip()

    # 2. Usage Baseline
    uses_tools = input("\nDo you incorporate QA/SAST tools into your development workflow?"\
    "(yes/no): ").lower().strip()

    if uses_tools == "yes":
        context = input("In what capacity? (Work, Personal Projects, Both): ").lower().strip()

        # Branch: Work Only
        if context == "work":
            is_helpful = input("Do you find them effective in a professional"\
            "environment? (yes/no): ").lower().strip()
            if is_helpful == "yes":
                input("Would you consider adopting them for personal use as well? (yes/no): ")
            else:
                input("What is the primary barrier to effectiveness?"\
                      "(Complexity, Noise/False Positives, Utility): ")

        # Branch: Personal Projects or Both
        elif context in ["personal projects", "both"]:
            frequency = input("How consistently do you use them? (Always, Often, Sometimes, Rarely): ")
            is_helpful = input("Do you find they provide significant value? (yes/no): ")

    else:
        # Branch: Non-users
        reason = input("\nWhat is the primary reason for not using these tools?"\
                       "\n(Lack of awareness, Trust issues, Cost, Alert fatigue): ")
        consideration = input("Would you consider integrating them if"\
        "these barriers were addressed? (yes/no): ")

    print("\nThank you for your professional feedback!")

if __name__ == "__main__":
    run_survey()
