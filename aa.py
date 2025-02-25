import requests
import numpy as np
import matplotlib.pyplot as plt

def fetch_global_market_data():
    # Placeholder for real API calls
    global_markets = {
        "S&P 500": 0.46,  # Change in percentage
        "Nasdaq 100": -1.17,
        "Dow Jones": 0.09,
        "SGX Nifty": 0.05,
    }
    return global_markets

def fetch_indian_market_data():
    # Placeholder for real API calls
    indian_markets = {
        "Nifty 50": 0.09,
        "Bank Nifty": 0.15,
        "India VIX": -0.02,
    }
    return indian_markets

def calculate_sentiment(global_data, indian_data):
    global_score = np.mean(list(global_data.values())) * 100  # Normalize
    indian_score = np.mean(list(indian_data.values())) * 100
    return global_score, indian_score

def visualize_sentiment(global_score, indian_score):
    labels = ['Global Sentiment', 'Indian Market Health']
    scores = [global_score, indian_score]
    colors = ['green' if s > 50 else 'red' if s < 30 else 'yellow' for s in scores]
    
    plt.figure(figsize=(6,4))
    plt.bar(labels, scores, color=colors)
    plt.ylim(0, 100)
    plt.ylabel("Sentiment Score")
    plt.title("Market Sentiment Analysis")
    plt.show()

def main():
    global_data = fetch_global_market_data()
    indian_data = fetch_indian_market_data()
    global_score, indian_score = calculate_sentiment(global_data, indian_data)
    visualize_sentiment(global_score, indian_score)

if __name__ == "__main__":
    main()
