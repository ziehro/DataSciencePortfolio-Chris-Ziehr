import numpy as np
from scipy.fft import fft
from sklearn.cluster import DBSCAN
from sklearn.preprocessing import StandardScaler

class MyceliumAI:
    def __init__(self, eps=0.5, min_samples=5):
        """
        Initialize the unsupervised learning module for live sensor data.
        
        :param eps: The maximum distance between two samples for them to be considered as in the same neighborhood.
        :param min_samples: The number of samples in a neighborhood for a point to be considered as a core point.
        """
        self.eps = eps
        self.min_samples = min_samples
        self.data = np.array([]).reshape(0, 2)  # Initialize an empty array for two features

    def update_data(self, new_data):
        # Append new data
        self.data = np.append(self.data, [[new_data, 0]], axis=0)
        
        # Update the second feature (FFT) dynamically
        if len(self.data) >= 30:  # Use a sliding window for FFT calculation
            fft_values = np.abs(fft(self.data[-30:, 0]))
            self.data[-30:, 1] = fft_values[:30]  # Update the second feature with FFT results
    
    def preprocess_features(self):
        """
        Preprocess features for clustering.
        """
        if len(self.data) > 0:
            # Standardize features
            scaler = StandardScaler()
            scaled_features = scaler.fit_transform(self.data)
            return scaled_features
        else:
            return np.array([]).reshape(0, 2)

    def detect_patterns(self):
        """
        Use DBSCAN to detect patterns in the preprocessed data.
        Returns a set of unique clusters detected.
        """
        scaled_features = self.preprocess_features()
        unique_clusters = set()
        if len(scaled_features) > 0:
            dbscan = DBSCAN(eps=self.eps, min_samples=self.min_samples)
            dbscan.fit(scaled_features)
            labels = dbscan.labels_
            
            # Identify unique clusters excluding noise (if label == -1)
            unique_clusters = set(labels) - {-1}
            print(f"Detected patterns (clusters): {unique_clusters}")

            # Optionally, reset data after processing to start fresh
            self.data = np.array([]).reshape(0, 2)
        
        return unique_clusters 
