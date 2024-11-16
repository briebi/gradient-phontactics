import collections
import math

# default dictionaries for trigrams and log probabilities of words
trigram_counts = collections.defaultdict(int)
word_probs = collections.defaultdict(float)

# empty list for words
words = []

with open('ukwords.phon', 'r') as file:
    for line in file:
        # adding boundary for each word and adding it to list
        word = line.strip()
        word_b = f'#{word}#'
        words.append(word_b)

        # making trigrams for word
        for i in range(len(word_b) - 2):
            trigram = word_b[i:i + 3]
            trigram_counts[trigram] += 1  # count trigram

# print some of trigrams and their counts to see if correct
print("Trigram Counts Sample: \n")
for trigram, count in list(trigram_counts.items())[:10]:
    print(f"{trigram}: {count}")

# total number of trigrams
total_trigrams = sum(trigram_counts.values())

# calculate log probabilities
for trigram, count in trigram_counts.items():
    probability = math.log(count / total_trigrams)
    # replacing count in dict with log prob
    trigram_counts[trigram] = probability

# sort trigrams by log probability and print
sorted_trigrams = sorted(trigram_counts.items(), key=lambda x: x[1])
print("Trigrams Sorted By Log Probability:\n")
for trigram in sorted_trigrams:
    print(f"{trigram}: {trigram_counts[trigram]}\n")

# average per-phoneme log probabilities for each word
for word in words:
    p_sum = 0.0
    tri_num = len(word) - 2

    # iterating through trigrams
    for i in range(tri_num):
        trigram = word[i:i + 3]
        p_sum += trigram_counts[trigram]

    avg = 0
    if tri_num > 0:
        avg = p_sum / tri_num

    word_probs[word] = avg  # store

# sort by avg per-phoneme log probability
sorted_probs = sorted(word_probs.items(), key=lambda x: x[1])

print("Average Per Phoneme Probabilities:\n")
for word, log_prob in sorted_probs:
    print(f"{word}: {log_prob}\n")
