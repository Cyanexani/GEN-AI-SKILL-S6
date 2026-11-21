from collections import Counter

word_freq = {"low": 5, "lower": 2, "newest": 3, "widest": 6}


def initialize_tokens(word_freq):
    out = {}
    for word in word_freq:
        out[word] = [word[0]] + ["##" + c for c in word[1:]]
    return out


def calculate_frequencies(tokenized_words, word_freq):
    token_freq = Counter()
    pair_freq = Counter()
    for word, tokens in tokenized_words.items():
        frequency = word_freq[word]
        for token in tokens:
            token_freq[token] += frequency
        for i in range(len(tokens) - 1):
            pair_freq[(tokens[i], tokens[i + 1])] += frequency
    return token_freq, pair_freq


def calculate_scores(token_freq, pair_freq):
    return {p: f / (token_freq[p[0]] * token_freq[p[1]]) for p, f in pair_freq.items()}


def merge_tokens(tokenized_words, best_pair):
    first, second = best_pair
    merged_token = first + second[2:] if second.startswith("##") else first + second
    for word, tokens in tokenized_words.items():
        new_tokens = []
        i = 0
        while i < len(tokens):
            if i < len(tokens) - 1 and tokens[i] == first and tokens[i + 1] == second:
                new_tokens.append(merged_token)
                i += 2
            else:
                new_tokens.append(tokens[i])
                i += 1
        tokenized_words[word] = new_tokens
    return merged_token


def wordpiece_training(word_freq):
    tokenized_words = initialize_tokens(word_freq)
    print("INITIAL TOKENIZATION")
    for word, tokens in tokenized_words.items():
        print(word, ":", tokens)
    iteration = 1
    while True:
        token_freq, pair_freq = calculate_frequencies(tokenized_words, word_freq)
        if not pair_freq:
            break
        scores = calculate_scores(token_freq, pair_freq)
        best_pair = max(scores, key=scores.get)
        print("\nIteration:", iteration)
        print("Selected Pair:", best_pair)
        print("Pair Frequency:", pair_freq[best_pair])
        print("WordPiece Score:", round(scores[best_pair], 6))
        print("Merged Token:", merge_tokens(tokenized_words, best_pair))
        iteration += 1
    print("\nFINAL TOKENIZATION")
    for word, tokens in tokenized_words.items():
        print(word, ":", tokens)


wordpiece_training(word_freq)
