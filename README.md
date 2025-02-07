## WLAN-Throughput-Prediction
<img width="665" alt="截屏2025-02-07 11 26 06" src="https://github.com/user-attachments/assets/d9cbf751-8d20-4eaf-b842-ed57525bccef" />

### Description:
This project aimed to predict throughput in Wireless Local Area Networks (WLANs) by analyzing key performance indicators and constructing predictive models based on real measurement data. The goal was to optimize throughput prediction and identify critical influencing factors.
#### 1. Problem 1: Throughput Prediction using BP Neural Network
To predict the throughput of WLAN access points (APs), I developed and compared five regression models and a BP neural network model. The BP neural network, which considered parameters such as network topology, business traffic, threshold values, and inter-node RSSI, was selected after five-fold cross-validation for model optimization. The BP model achieved an accuracy of 0.9675 and **R² = 0.9425**. The key influencing factors, ranked by feature importance, were: inter-node **RSSI > Access Control Mechanism > Data Length**.
#### 2. Problem 2: Modulation and Coding Scheme (MCS) and Spatial Streams Prediction
I developed a tree-based predictive model for selecting the Modulation and Coding Scheme (MCS) and spatial streams (NSS) during data transmission in WLAN networks. Using machine learning algorithms like **Random Forest, XGBoost, and CatBoost**, the CatBoost model was found to have the best prediction accuracy, achieving an RMSE of 16.89 and R² = 0.915 on the test set. The feature importance ranking for this model was: inter-node **RSSI > Network Topology > Business Traffic > Threshold Information**.
#### 3. Problem 3: Optimizing Throughput Prediction Using Hybrid Algorithms
To enhance throughput prediction, I combined **Genetic Algorithm**, **Particle Swarm Optimization**, and **Grid Search** with a neural network model. The model considered AP transmission opportunities, PHY Rate, and data frame bit count. By integrating global search capabilities of Genetic Algorithms and local search of Particle Swarm Optimization, the model's prediction ability and stability were improved in complex network environments. The final model achieved RMSE = 13 and **R² = 0.94** for the test set.
### Technologies Used:
BP Neural Network, Random Forest, XGBoost, CatBoost, Genetic Algorithm, Particle Swarm Optimization, Grid Search
### Skills: 
Feature Engineering, Model Optimization, Predictive Analytics, Machine Learning, Data Visualization, Statistical Analysis

<img width="588" alt="截屏2025-02-07 11 28 05" src="https://github.com/user-attachments/assets/80cf583a-1944-4212-bc52-572f21d8799e" />
<img width="684" alt="截屏2025-02-07 11 27 36" src="https://github.com/user-attachments/assets/01faa7a2-73d1-4bc9-a977-91b247524e70" />

<img width="691" alt="截屏2025-02-07 11 25 15" src="https://github.com/user-attachments/assets/d24e704c-4bed-4432-8651-78aa91eb1b67" />
