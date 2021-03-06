# Bubble Factory exercise

# scores = results from the bubble tests
# costs = cost of the test in the parallel list scores[]
scores = [60, 50, 60, 58, 54, 54,
            58, 50, 52, 54, 48, 69,
            34, 55, 51, 52, 44, 51,
            69, 64, 66, 55, 52, 61,
            46, 31, 57, 52, 44, 18,
            41, 53, 55, 61, 51, 44]

costs = [.25, .27, .25, .25, .25, .25,
            .33, .31, .25, .29, .27, .22,
            .31, .25, .25, .33, .21, .25,
            .25, .25, .28, .25, .24, .22,
            .20, .25, .30, .25, .24, .25,
            .25, .25, .27, .25, .26, .29]

# Iterates through list 'scores' once to find the high_score:
high_score = 0
length = len(scores)
for i in range(length):
    if scores[i] > high_score:
        high_score = scores[i]

# For loop finds all tests that match high_score, adds them to list best_solutions:
best_solutions = []
for i in range(length):
    if high_score == scores[i]:
        best_solutions.append(i)

# For loop determines most effective bubble test by looking for
# lowest cost and high_score to produce most_effective:
cost = 100.0
most_effective = 0
for i in range(length):
    if scores[i] == high_score and costs[i] < cost:
        most_effective = i
        cost = costs[i]

# Print the results: number of tests, high_score, best_solutions, most_effective:
print('Bubble tests:', length)
print('Highest bubble test score:', high_score)
print('Tests with the highest score:', best_solutions)
print('Bubble test', most_effective, 'is the best one with a cost of', costs[most_effective])

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