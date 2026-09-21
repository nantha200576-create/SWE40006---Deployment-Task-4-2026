import sys
from collections import Counter
import string

def process_data():
    print("=====================================================")
    print("   ADVANCED PYTHON DATA PROCESSOR (Task 4.4 HD)      ")
    print("=====================================================")
    
    # Sample multi-sentence dataset simulating a text analytics pipeline
    sample_texts = [
        "Docker containerization makes software deployment reliable, scalable, and efficient.",
        "Containerized applications run in isolated user spaces called containers.",
        "Ensuring high availability and error handling is critical for modern software systems."
    ]
    
    print(f"[INFO] Loaded {len(sample_texts)} records for processing...\n")
    
    full_corpus = " ".join(sample_texts)
    
    # 1. Basic Metrics
    total_characters_with_spaces = len(full_corpus)
    total_characters_no_spaces = len(full_corpus.replace(" ", ""))
    words = full_corpus.translate(str.maketrans('', '', string.punctuation)).lower().split()
    total_words = len(words)
    total_sentences = len(sample_texts)
    
    # 2. Advanced Analytics: Most common words
    word_counts = Counter(words)
    most_common = word_counts.most_common(3)
    
    # 3. Average word length calculation
    avg_word_length = sum(len(word) for word in words) / total_words if total_words > 0 else 0

    # Output Structured Results
    print("--- Text Analysis Report ---")
    print(f" • Total Sentences       : {total_sentences}")
    print(f" • Total Words           : {total_words}")
    print(f" • Characters (incl. spaces): {total_characters_with_spaces}")
    print(f" • Characters (excl. spaces): {total_characters_no_spaces}")
    print(f" • Average Word Length   : {avg_word_length:.2f} characters")
    print("\n--- Top 3 Most Frequent Keywords ---")
    for word, freq in most_common:
        print(f"   - '{word}': {freq} occurrences")
        
    print("\n=====================================================")
    print("   DATA PROCESSING & PIPELINE COMPLETED SUCCESSFULLY!  ")
    print("=====================================================")

if __name__ == "__main__":
    process_data()