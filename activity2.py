class_scores = {
    "lily": 10,
    "daniela": 25,
    "lisa": 20,
    "ava": 50,
    "lara": 30
}

sorted_class = sorted(class_scores.items(), key=lambda item: item[1], reverse=True)

print("--- CLASS LEADERBOARD ---")
for student, score in sorted_class:
    print(f"{student.title()}: {score} points")
