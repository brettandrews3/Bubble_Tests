# Bubble Factory exercise

# Scores = results from the bubble tests
scores = [60, 50, 60, 58, 54, 54,
            58, 50, 52, 54, 48, 69,
            34, 55, 51, 52, 44, 51,
            69, 64, 66, 55, 52, 61,
            46, 31, 57, 52, 44, 18,
            41, 53, 55, 61, 51, 44]

# Iterates through list 'scores' once to find the high_score:
high_score = 0
length = len(scores)
for i in range(length):
    if scores[i] > high_score:
        high_score = scores[i]

# Write while loop to iterate through 'scores' list...:
"""
# While loop to print 'Bubble solution #i score: i':
i = 0
length = len(scores)
while i < length:
    print('Bubble solution #' + str(i), 'score:', scores[i])
    i = i + 1
"""

# ...and here's the for loop version of that while statement:
i = 0
for score in scores:
    output = 'Bubble solution #' + str(i) + ': ' + str(score)
    print(output)
    i = i + 1

#TODO Return to print calculated averages
# Prints number of tests and high_score from the list 'scores':
print('Bubble tests:', len(scores), '\n')
print('The highest bubble score is:', high_score)