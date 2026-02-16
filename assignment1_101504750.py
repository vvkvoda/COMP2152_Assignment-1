"""
Author: Vaishnavi Vodapalli
Assignment: #1
Description: Workout tracking system for gym friends
"""

# Step b: Create 4 variables with data type comments
gym_member = "Vaishnavi Vodapalli"  # string
preferred_weight_kg = 50.5           # float
highest_reps = 25                    # integer
membership_active = True              # boolean

# Step c: Create a dictionary named workout_stats
# Data type: dictionary with string keys and tuple values
workout_stats = {
    "Alex": (30, 45, 20),     # yoga, running, weightlifting minutes
    "Jamie": (25, 35, 40),
    "Taylor": (40, 30, 25)
}

# Step d: Calculate total workout minutes using a loop and add to dictionary
# Create a copy of the keys to iterate over to avoid dictionary size change error
friend_names = list(workout_stats.keys())
for friend in friend_names:
    minutes = workout_stats[friend]
    total_minutes = sum(minutes)
    workout_stats[f"{friend}_Total"] = total_minutes

# Display workout_stats after adding totals
print("Workout Statistics Dictionary:")
for key, value in workout_stats.items():
    print(f"  {key}: {value}")

# Step e: Create a 2D nested list called workout_list
# Data type: list of lists (2-dimensional array)
workout_list = [
    list(workout_stats["Alex"]),
    list(workout_stats["Jamie"]),
    list(workout_stats["Taylor"])
]

print("\n2D Workout List (yoga, running, weightlifting):")
for row in workout_list:
    print(f"  {row}")

# Step f: Slice the workout_list

# Extract and print minutes for yoga and running for all friends
print("\nYoga and running minutes for all friends:")
yoga_running_slice = [row[:2] for row in workout_list]  # First two columns
for friend_slice in yoga_running_slice:
    print(f"  {friend_slice}")

# Extract and print minutes for weightlifting for the last two friends
print("\nWeightlifting minutes for last two friends:")
weightlifting_slice = [row[2] for row in workout_list[-2:]]  # Last column for last two rows
for minutes in weightlifting_slice:
    print(f"  {minutes}")

# Step g: Check if any friend's total >= 120
print("\nActivity Check:")
friend_names = ["Alex", "Jamie", "Taylor"]
for friend in friend_names:
    total = workout_stats[f"{friend}_Total"]
    if total >= 120:
        print(f"  Great job staying active, {friend}!")

# Step h: User input to look up a friend (case-insensitive version)
print("\n" + "="*50)
print("FRIEND WORKOUT LOOKUP")
print("="*50)

user_input = input("Enter a friend's name to check their workout stats (Alex, Jamie, or Taylor): ")

# Capitalize first letter for case-insensitive matching
formatted_input = user_input.capitalize()

if formatted_input in friend_names:
    minutes = workout_stats[formatted_input]
    total = workout_stats[f"{formatted_input}_Total"]
    print(f"\n{formatted_input}'s Workout Summary:")
    print(f"  Yoga: {minutes[0]} minutes")
    print(f"  Running: {minutes[1]} minutes")
    print(f"  Weightlifting: {minutes[2]} minutes")
    print(f"  TOTAL: {total} minutes")
else:
    print(f"\nFriend '{user_input}' not found in the records.")
    
# Step i: Friend with highest and lowest total workout minutes
print("\n" + "="*50)
print("WORKOUT STATISTICS SUMMARY")
print("="*50)

# Calculate totals for each friend
friend_totals = {}
for friend in friend_names:
    friend_totals[friend] = workout_stats[f"{friend}_Total"]

# Find highest and lowest
highest_friend = max(friend_totals, key=friend_totals.get)
lowest_friend = min(friend_totals, key=friend_totals.get)

print(f"\nFriend with highest total workout minutes:")
print(f"  {highest_friend}: {friend_totals[highest_friend]} minutes")

print(f"\nFriend with lowest total workout minutes:")
print(f"  {lowest_friend}: {friend_totals[lowest_friend]} minutes")

# Additional: Show all friends' totals
print("\nAll Friends' Total Minutes:")
for friend in friend_names:
    print(f"  {friend}: {friend_totals[friend]} minutes")

print("\n" + "="*50)
print("Program completed successfully!")