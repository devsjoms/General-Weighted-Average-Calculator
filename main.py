import customtkinter as ctk
from tkinter import messagebox


ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

app = ctk.CTk()
app.title("GWA Calculator")
app.geometry("850x750")
app.minsize(700, 600)

subject_entries = []

def toggle_theme():
    if appearance_switch.get() == 1:
        ctk.set_appearance_mode("light")
    else:
        ctk.set_appearance_mode("dark")
def show_subject_inputs():

    for widget in subjects_frame.winfo_children():
        widget.destroy()

    subject_entries.clear()

    try:
        subject_count = int(subject_count_entry.get())

        if subject_count < 1 or subject_count > 12:
            messagebox.showerror(
                "Invalid Input",
                "Please enter between 1 and 12 subjects."
            )
            return

    except ValueError:
        messagebox.showerror(
            "Invalid Input",
            "Please enter a valid number of subjects."
        )
        return

    for i in range(subject_count):

        subject_card = ctk.CTkFrame(
            subjects_frame,
            corner_radius=12
        )

        subject_card.pack(
            fill="x",
            padx=10,
            pady=8
        )

        subject_title = ctk.CTkLabel(
            subject_card,
            text=f"Subject {i + 1}",
            font=("Arial", 16, "bold")
        )

        subject_title.grid(
            row=0,
            column=0,
            columnspan=3,
            sticky="w",
            padx=20,
            pady=(15, 10)
        )

        course_label = ctk.CTkLabel(
            subject_card,
            text="Course Name"
        )

        course_label.grid(
            row=1,
            column=0,
            sticky="w",
            padx=(20, 5)
        )

        course_entry = ctk.CTkEntry(
            subject_card,
            placeholder_text="e.g. IT101"
        )

        course_entry.grid(
            row=2,
            column=0,
            sticky="ew",
            padx=(20, 10),
            pady=(5, 20)
        )


        units_label = ctk.CTkLabel(
            subject_card,
            text="Units"
        )

        units_label.grid(
            row=1,
            column=1,
            sticky="w",
            padx=5
        )

        units_entry = ctk.CTkEntry(
            subject_card,
            placeholder_text="e.g. 3"
        )

        units_entry.grid(
            row=2,
            column=1,
            sticky="ew",
            padx=5,
            pady=(5, 20)
        )


        grade_label = ctk.CTkLabel(
            subject_card,
            text="Grade"
        )

        grade_label.grid(
            row=1,
            column=2,
            sticky="w",
            padx=(5, 20)
        )

        grade_entry = ctk.CTkEntry(
            subject_card,
            placeholder_text="e.g. 1.50"
        )

        grade_entry.grid(
            row=2,
            column=2,
            sticky="ew",
            padx=(5, 20),
            pady=(5, 20)
        )

        subject_card.grid_columnconfigure(
            0,
            weight=3
        )

        subject_card.grid_columnconfigure(
            1,
            weight=1
        )

        subject_card.grid_columnconfigure(
            2,
            weight=1
        )

        subject_entries.append(
            (
                course_entry,
                units_entry,
                grade_entry
            )
        )

    calculate_button.pack(
        pady=20
    )
def compute_grades():

    total_units = 0
    computed_average = 0

    try:

        for course_entry, units_entry, grade_entry in subject_entries:

            course = course_entry.get().strip()
            units_text = units_entry.get().strip()
            grade_text = grade_entry.get().strip()

            if not course or not units_text or not grade_text:

                messagebox.showerror(
                    "Incomplete Input",
                    "Please complete all subject fields."
                )

                return

            units = int(units_text)
            grade = float(grade_text)

            if units <= 0:

                messagebox.showerror(
                    "Invalid Units",
                    f"Units for {course} must be greater than 0."
                )

                return

            if grade < 1.00 or grade > 5.00:

                messagebox.showerror(
                    "Invalid Grade",
                    f"Grade for {course} must be between 1.00 and 5.00."
                )

                return

            total_units += units

            computed = grade * units

            computed_average += computed

        computed_gwa = computed_average / total_units

        show_result(
            computed_gwa,
            total_units
        )

    except ValueError:

        messagebox.showerror(
            "Invalid Input",
            "Units must be whole numbers and grades must be numeric."
        )
def show_result(gwa, total_units):

    for widget in subjects_frame.winfo_children():
        widget.destroy()

    calculate_button.pack_forget()

    result_card = ctk.CTkFrame(
        subjects_frame,
        corner_radius=20
    )

    result_card.pack(
        fill="x",
        padx=20,
        pady=30
    )

    result_title = ctk.CTkLabel(
        result_card,
        text="YOUR GWA",
        font=("Arial", 18, "bold")
    )

    result_title.pack(
        pady=(30, 5)
    )

    gwa_label = ctk.CTkLabel(
        result_card,
        text=f"{gwa:.2f}",
        font=("Arial", 52, "bold")
    )

    gwa_label.pack(
        pady=10
    )

    subjects_label = ctk.CTkLabel(
        result_card,
        text=f"Total Subjects: {len(subject_entries)}"
    )

    subjects_label.pack(
        pady=5
    )

    units_label = ctk.CTkLabel(
        result_card,
        text=f"Total Units: {total_units}"
    )

    units_label.pack(
        pady=(0, 30)
    )

    reset_button = ctk.CTkButton(
        subjects_frame,
        text="Calculate Again",
        command=reset_calculator,
        height=45,
        corner_radius=10
    )

    reset_button.pack(
        pady=10
    )
def reset_calculator():

    for widget in subjects_frame.winfo_children():
        widget.destroy()

    subject_entries.clear()

    subject_count_entry.delete(
        0,
        "end"
    )

    calculate_button.pack_forget()
header = ctk.CTkFrame(
    app,
    fg_color="transparent"
)
header.pack(
    fill="x",
    padx=40,
    pady=(25, 10)
)
header_left = ctk.CTkFrame(
    header,
    fg_color="transparent"
)
header_left.pack(
    side="left"
)
title = ctk.CTkLabel(
    header_left,
    text="GWA Calculator",
    font=("Arial", 32, "bold")
)
title.pack(
    anchor="w"
)
subtitle = ctk.CTkLabel(
    header_left,
    text="Calculate your General Weighted Average",
    font=("Arial", 15)
)
subtitle.pack(
    anchor="w",
    pady=(5, 0)
)
header_right = ctk.CTkFrame(
    header,
    fg_color="transparent"
)
header_right.pack(
    side="right"
)
theme_label = ctk.CTkLabel(
    header_right,
    text="Light Mode"
)
theme_label.pack(
    side="left",
    padx=(0, 10)
)
appearance_switch = ctk.CTkSwitch(
    header_right,
    text="",
    command=toggle_theme
)
appearance_switch.pack(
    side="left"
)
count_frame = ctk.CTkFrame(
    app,
    corner_radius=15
)
count_frame.pack(
    fill="x",
    padx=40,
    pady=15
)
count_label = ctk.CTkLabel(
    count_frame,
    text="Number of Subjects",
    font=("Arial", 15, "bold")
)
count_label.pack(
    anchor="w",
    padx=20,
    pady=(20, 5)
)
subject_count_entry = ctk.CTkEntry(
    count_frame,
    placeholder_text="Enter 1 - 12",
    height=40
)
subject_count_entry.pack(
    fill="x",
    padx=20,
    pady=10
)
continue_button = ctk.CTkButton(
    count_frame,
    text="Continue",
    command=show_subject_inputs,
    height=40,
    corner_radius=10
)
continue_button.pack(
    padx=20,
    pady=(5, 20)
)
subjects_frame = ctk.CTkScrollableFrame(
    app,
    label_text="Subjects"
)
subjects_frame.pack(
    fill="both",
    expand=True,
    padx=40,
    pady=10
)
calculate_button = ctk.CTkButton(
    app,
    text="Calculate GWA",
    command=compute_grades,
    height=45,
    corner_radius=10
)
app.mainloop()