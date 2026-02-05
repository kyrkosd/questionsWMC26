
import customtkinter as ctk

# --- 1. GLOBAL DATA ---
results = {}
current_step = "uses_tools"

# --- 2. LOGIC FUNCTIONS ---
def handle_click(choice):
    """Processes the answer and decides what to show next."""
    global current_step
    results[current_step] = choice

    # Following your original script's logic:
    if current_step == "uses_tools":
        if choice == "Yes":
            show_step("context", "What for?", ["Work", "Personal Projects", "Both"])
        else:
            show_step("barrier", "Why not?", ["Unknown", "Lack of trust", "Expensive", "Noise"])

    elif current_step == "context":
        show_step("benefit", "What problems do they solve?"\
                  , ["Vulnerabilities", "Code Quality", "Both", "None"])

    elif current_step == "benefit":
        if choice == "None":
            show_step("reason_why_none", "Why not?"\
                      , ["Too complex", "Not useful", "Too much noise", "Unsure"])
        else:
            show_step("frequency", "How often?", ["Always", "Often", "Sometimes", "Rarely"])

    elif current_step == "barrier":
        show_step("future_use", "Would you consider them later?", ["Yes", "No"])

    # If we hit these, the next step is the Rating Slider
    elif current_step in ["frequency", "reason_why_none", "future_use"]:
        show_rating_screen()

def show_step(step_id, question_text, options):
    """Clears old buttons and draws new ones for the current question."""
    global current_step
    current_step = step_id

    # Update text
    main_label.configure(text=question_text)

    # Clear old buttons
    for widget in button_frame.winfo_children():
        widget.destroy()

    # Create new buttons
    for opt in options:
        btn = ctk.CTkButton(button_frame, text=opt, command=lambda o=opt: handle_click(o))
        btn.pack(pady=10, padx=20, fill="x")

def show_rating_screen():
    """Shows the 1-10 rating scale."""
    global current_step
    current_step = "rating"

    main_label.configure(text="How do you evaluate them from 1-10?")

    for widget in button_frame.winfo_children():
        widget.destroy()

    # Create a slider
    slider = ctk.CTkSlider(button_frame, from_=1, to=10, number_of_steps=9)
    slider.set(5)
    slider.pack(pady=20)

    # Show the number value
    val_label = ctk.CTkLabel(button_frame, text="Current Rating: 5")
    val_label.pack()
    slider.configure(command=lambda v: val_label.configure(text=f"Current Rating: {int(v)}"))

    # Final Submit Button
    submit_btn = ctk.CTkButton(button_frame, text="Finish Survey", 
                        command=lambda: finish(slider.get()))
    submit_btn.pack(pady=20)

def finish(final_rating):
    results['rating'] = int(final_rating)
    main_label.configure(text="Submission successful!\nThank you for participating.")
    button_frame.destroy()

    print("\n--- SURVEY RESULTS ---")
    for key, val in results.items():
        print(f"{key}: {val}")

# --- 3. UI INITIALIZATION ---
ctk.set_appearance_mode("dark")  # Modern dark mode
app = ctk.CTk()
app.geometry("500x500")
app.title("Security & Quality Survey")

# Title
title = ctk.CTkLabel(app, text="SOFTWARE SECURITY SURVEY", font=("Arial", 22, "bold"))
title.pack(pady=30)

# Question Label
main_label = ctk.CTkLabel(app, text="Do you use QA/SAST tools?", font=("Arial", 16), wraplength=400)
main_label.pack(pady=10)

# Container for buttons
button_frame = ctk.CTkFrame(app, fg_color="transparent")
button_frame.pack(pady=20, fill="both", expand=True)

# Start with first question buttons
for option in ["Yes", "No"]:
    b = ctk.CTkButton(button_frame, text=option, command=lambda o=option: handle_click(o))
    b.pack(pady=10, padx=20, fill="x")

app.mainloop()
