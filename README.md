# README: Trigram Probability Analysis

## Overview

This Python script analyzes the trigram (three-character sequence) probabilities of words derived from a phonetic word list. It computes log probabilities for trigrams, determines the average per-phoneme log probability for each word, and outputs sorted results.

The script is intended for natural language processing (NLP) tasks where phoneme-based analysis is relevant, such as speech recognition, linguistic research, or language modeling.

---

## Features

1. **Trigram Counts**:  
   Calculates the frequency of all trigrams in the provided word list.
   
2. **Log Probabilities**:  
   Computes the log probabilities for each trigram based on their relative frequency.

3. **Word-Level Analysis**:  
   Calculates the average per-phoneme log probability for each word.

4. **Sorting and Display**:  
   Outputs:
   - Trigrams and their counts (sampled).
   - Trigrams sorted by log probability.
   - Words sorted by average per-phoneme log probability.

---

## Prerequisites

- Python 3.x

---

## Setup Instructions

1. **Install Python**:  
   Ensure Python 3.x is installed on your machine.  
   [Download Python](https://www.python.org/downloads/)

2. **Prepare Word File**:  
   Create or obtain a file named `ukwords.phon`, ensuring it contains one word per line.

3. **Run the Script**:  
   Execute the script in your Python environment. For example:  
   ```bash
   python trigram_analysis.py
