# Energy Consumption Forecasting (Time Series)

This project focuses on forecasting hourly energy consumption using time series machine learning techniques. The goal is to analyze historical energy usage patterns and build a predictive model capable of estimating future consumption.

---

## Project Overview

Energy consumption data contains strong daily, weekly, and seasonal patterns. In this project:

- Exploratory Data Analysis (EDA) is performed to understand trends and seasonality
- Time-based and lag features are engineered
- Multiple machine learning models are trained and compared
- The best-performing model is saved for deployment

The final model is designed to be deployable in a Streamlit app or HuggingFace Space.

---

## Dataset

Dataset source: Kaggle  
Hourly Energy Consumption Dataset

The dataset includes:

- Hourly timestamps
- Energy consumption in megawatts (MW)
- Multi-year time span (~14 years)

Only the **AEP region** is used to keep the project focused and interpretable.

---

## Workflow

1. Data Loading
2. Data Inspection & Cleaning
3. Exploratory Data Analysis (EDA)
4. Feature Engineering
5. Model Building
6. Model Evaluation
7. Forecast Visualization
8. Model Saving

---

## Models Used

### XGBoost (Final Model)
- Best performance
- Captures nonlinear time dependencies
- Selected as final deployable model

### Random Forest
- Used for model comparison
- Slightly lower accuracy than XGBoost

---

## Model Performance

| Model | MAE | RMSE |
|------|------|------|
| XGBoost | ~136 | ~181 |
| Random Forest | ~147 | ~197 |

XGBoost achieved the best forecasting accuracy and was selected as the final model.

---

## Technologies

- Python
- Pandas
- NumPy
- Matplotlib / Seaborn
- Scikit-learn
- XGBoost
- Streamlit
- Joblib

---

## Model Saving

The trained model is saved as:energy_forecast_xgboost.pkl
-----------------------------------------------------------------------------------------

# Enerji Tüketimi Tahmini (Zaman Serisi)

Bu proje, saatlik enerji tüketimini zaman serisi makine öğrenmesi yöntemleri ile tahmin etmeyi amaçlamaktadır. Amaç, geçmiş enerji kullanım örüntülerini analiz ederek gelecekteki tüketimi tahmin edebilen bir model geliştirmektir.

---

## Proje Özeti

Enerji tüketim verileri güçlü günlük, haftalık ve mevsimsel örüntüler içerir. Bu projede:

- Keşifsel Veri Analizi (EDA) yapılmıştır
- Zaman tabanlı ve gecikmeli (lag) özellikler üretilmiştir
- Birden fazla makine öğrenmesi modeli eğitilmiştir
- Modeller karşılaştırılmış ve en iyi model seçilmiştir
- Nihai model deployment için kaydedilmiştir

Model Streamlit veya HuggingFace ortamında çalıştırılabilecek şekilde hazırlanmıştır.

---

## Veri Seti

Kaynak: Kaggle  
Saatlik Enerji Tüketimi Veri Seti

Veri seti şunları içerir:

- Saatlik zaman damgaları
- Megawatt (MW) cinsinden enerji tüketimi
- Yaklaşık 14 yıllık zaman aralığı

Projede analiz sade tutulmak amacıyla yalnızca **AEP bölgesi** kullanılmıştır.

---

## İş Akışı

1. Veri Yükleme
2. Veri İnceleme ve Temizleme
3. Keşifsel Veri Analizi (EDA)
4. Özellik Mühendisliği
5. Model Kurulumu
6. Model Değerlendirme
7. Tahmin Görselleştirme
8. Model Kaydetme

---

## Kullanılan Modeller

### XGBoost (Nihai Model)
- En iyi performansı göstermiştir
- Karmaşık örüntüleri öğrenebilir
- Deployment için seçilmiştir

### Random Forest
- Model karşılaştırması için kullanılmıştır
- XGBoost’a göre biraz daha düşük performans göstermiştir

---

## Model Performansı

| Model | MAE | RMSE |
|------|------|------|
| XGBoost | ~136 | ~181 |
| Random Forest | ~147 | ~197 |

XGBoost en yüksek doğruluğu sağladığı için nihai model olarak seçilmiştir.

---

## Kullanılan Teknolojiler

- Python
- Pandas
- NumPy
- Matplotlib / Seaborn
- Scikit-learn
- XGBoost
- Streamlit
- Joblib

---

## Model Kaydı

Eğitilmiş model şu dosya olarak kaydedilmiştir:energy_forecast_xgboost.pkl


