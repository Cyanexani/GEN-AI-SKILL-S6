from collections import Counter

word_freq = {"low": 5, "lower": 2, "newest": 3, "widest": 6}


def initialize_tokens(word_freq):
    return {word: list(word) for word in word_freq}


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


def merge_tokens(tokenized_words, best_pair):
    first, second = best_pair
    merged_token = first + second
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


def bpe_training(word_freq):
    tokenized_words = initialize_tokens(word_freq)
    print("INITIAL TOKENIZATION")
    for word, tokens in tokenized_words.items():
        print(word, ":", tokens)
    iteration = 1
    while True:
        token_freq, pair_freq = calculate_frequencies(tokenized_words, word_freq)
        if not pair_freq:
            break
        best_pair = max(pair_freq, key=pair_freq.get)
        print("\nIteration:", iteration)
        print("Selected Pair:", best_pair)
        print("Pair Frequency:", pair_freq[best_pair])
        print("Merged Token:", merge_tokens(tokenized_words, best_pair))
        iteration += 1
    print("\nFINAL TOKENIZATION")
    for word, tokens in tokenized_words.items():
        print(word, ":", tokens)


bpe_training(word_freq)
