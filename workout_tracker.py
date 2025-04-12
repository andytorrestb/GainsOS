import pandas as pd
import os
import tkinter as tk
from tkinter import ttk, messagebox
from datetime import date

# Load existing dataframe if exists, otherwise create a new one
if os.path.exists('training_log.csv'):
    training_data = pd.read_csv('training_log.csv')
else:
    training_data = pd.DataFrame(columns=[
        'Date', 'Workout_Type', 'Exercise', 'Sets_Reps_or_Duration',
        'Weight_or_Intensity', 'Performance_Metrics', 'Pain_or_Discomfort_Level', 'Notes'
    ])

# Function to add a new workout entry
def add_workout_entry():
    global training_data
    new_entry = pd.DataFrame({
        'Date': [date.today().isoformat()],
        'Workout_Type': [workout_type_var.get()],
        'Exercise': [exercise_var.get()],
        'Sets_Reps_or_Duration': [sets_reps_entry.get()],
        'Weight_or_Intensity': [weight_var.get()],
        'Performance_Metrics': [performance_var.get()],
        'Pain_or_Discomfort_Level': [pain_var.get()],
        'Notes': [notes_entry.get()]
    })
    training_data = pd.concat([training_data, new_entry], ignore_index=True)
    training_data.to_csv('training_log.csv', index=False)
    messagebox.showinfo("Success", "Workout entry added successfully!")

# Simple GUI using Tkinter
app = tk.Tk()
app.title("Workout Logger")

# Predefined options
workout_types = ['Lower Body Strength', 'Conditioning/Core', 'Athleticism', 'Recovery']
exercises = ['Goblet Squat', 'Sprint Intervals', 'Box Jumps', 'Single-Leg Deadlift']
weights = ['Bodyweight', '35 lbs', '50 lbs', 'Moderate', 'Heavy']
performance_metrics = ['Form Good', 'Explosive', 'Stable Landing', 'Improved ROM']
pain_levels = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10']

# Labels and widgets
# Workout Type
tk.Label(app, text='Workout Type').grid(row=0, column=0, padx=5, pady=5, sticky='e')
workout_type_var = tk.StringVar()
workout_type_entry = ttk.Combobox(app, textvariable=workout_type_var, values=workout_types)
workout_type_entry.grid(row=0, column=1, padx=5, pady=5)
workout_type_entry['state'] = 'normal'

# Exercise
tk.Label(app, text='Exercise').grid(row=1, column=0, padx=5, pady=5, sticky='e')
exercise_var = tk.StringVar()
exercise_entry = ttk.Combobox(app, textvariable=exercise_var, values=exercises)
exercise_entry.grid(row=1, column=1, padx=5, pady=5)
exercise_entry['state'] = 'normal'

# Sets/Reps or Duration
tk.Label(app, text='Sets/Reps or Duration').grid(row=2, column=0, padx=5, pady=5, sticky='e')
sets_reps_entry = ttk.Entry(app, width=40)
sets_reps_entry.grid(row=2, column=1, padx=5, pady=5)

# Weight or Intensity
tk.Label(app, text='Weight or Intensity').grid(row=3, column=0, padx=5, pady=5, sticky='e')
weight_var = tk.StringVar()
weight_entry = ttk.Combobox(app, textvariable=weight_var, values=weights)
weight_entry.grid(row=3, column=1, padx=5, pady=5)
weight_entry['state'] = 'normal'

# Performance Metrics
tk.Label(app, text='Performance Metrics').grid(row=4, column=0, padx=5, pady=5, sticky='e')
performance_var = tk.StringVar()
performance_entry = ttk.Combobox(app, textvariable=performance_var, values=performance_metrics)
performance_entry.grid(row=4, column=1, padx=5, pady=5)
performance_entry['state'] = 'normal'

# Pain or Discomfort Level
tk.Label(app, text='Pain or Discomfort Level').grid(row=5, column=0, padx=5, pady=5, sticky='e')
pain_var = tk.StringVar()
pain_entry = ttk.Combobox(app, textvariable=pain_var, values=pain_levels)
pain_entry.grid(row=5, column=1, padx=5, pady=5)
pain_entry['state'] = 'normal'

# Notes
tk.Label(app, text='Notes').grid(row=6, column=0, padx=5, pady=5, sticky='e')
notes_entry = ttk.Entry(app, width=40)
notes_entry.grid(row=6, column=1, padx=5, pady=5)

# Submit Button
submit_btn = ttk.Button(app, text="Add Workout", command=add_workout_entry)
submit_btn.grid(row=7, column=0, columnspan=2, pady=10)

app.mainloop()
