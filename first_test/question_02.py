scores = [78, 92, 56, 88, 60, 45, 100]

print(sum(scores))
print(max(scores))
print(min(scores))

scores_number =[]
for score in scores:
    if score >= 60:
        scores_number.append(score)
print(len(scores_number))

scores_avg =[]
for score in scores:
    avg = sum(scores)/len(scores)
    if score >= avg:
        scores_avg.append(score)
print(scores_avg)