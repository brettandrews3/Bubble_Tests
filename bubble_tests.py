# Bubble Factory exercise

# Scores = results from the bubble tests
scores = [60, 50, 60, 58, 54, 54,
            58, 50, 52, 54, 48, 69,
            34, 55, 51, 52, 44, 51,
            69, 64, 66, 55, 52, 61,
            46, 31, 57, 52, 44, 18,
            41, 53, 55, 61, 51, 44]

# Here's a few print statements that pull from the list. Write while loop to iterate this:
"""
print('Bubble solution #0 score:', scores[0])
print('Bubble solution #1 score:', scores[1])
"""

"""
# While loop to print 'Bubble solution #i score: i':
i = 0
length = len(scores)
while i < length:
    print('Bubble solution #' + str(i), 'score:', scores[i])
    i = i + 1
"""

# For loop version of the same statement:
i = 0
for score in scores:
    output = 'Bubble solution #' + str(i) + ': ' + str(score)
    print(output)
    i = i + 1

#TODO Return to print calculated averages, scores[i] for highest values
print('Bubble tests:', len(scores))