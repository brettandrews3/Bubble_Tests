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



# This branch tests out a simplified index for loop to find the most
# cost-effective bubble test:
cost = 100.0                        # Using float because cost is a decimal value
most_effective = 0                  # Using int because we're looping through the list placements

for i in range(len(best_solutions)):            # Now iterating through a best_solutions list of 2 items.
    index = best_solutions[i]
    if cost > costs[index]:
        most_effective = index
        cost = costs[index]

print('Solution', most_effective,
        'is the most effective test with a cost of $' + str(costs[most_effective]) + '.')