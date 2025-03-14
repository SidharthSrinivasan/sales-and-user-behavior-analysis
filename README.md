# Sales and User Behavior Analysis

## 📌 Project Overview
This project simulates and analyzes sales and user behavior data using synthetic data generation, real-time data streaming with Apache Kafka, and data storage in PostgreSQL. Key business insights are derived using SQL-based metrics, and the results are visualized with Tableau.

---

## 🚀 Features
- **Synthetic Data Generation**: Realistic user transactions are generated using Faker.
- **Real-time Data Streaming**: Kafka is used to stream transaction data into PostgreSQL.
- **Data Storage & Processing**: PostgreSQL stores and processes sales data efficiently.
- **Key Metrics Calculation**: SQL queries extract insights such as top-selling products and user purchase behavior.
- **Interactive Visualizations**: Tableau dashboards provide a clear representation of key business insights.

---

## 🔧 Tech Stack
- **Python**: Data generation & Kafka producer/consumer
- **Apache Kafka**: Real-time data streaming
- **PostgreSQL**: Data storage & query processing
- **SQL**: Data aggregation & insights
- **Tableau**: Data visualization
- **Docker**: Containerized deployment

---

## 📂 Project Structure
```
Sales-and-User-Behavior-Analysis/
│── data_generation/
│   ├── generate.py            # Generates synthetic transaction data
│── data_streaming/
│   ├── kafka_producer.py      # Streams data to Kafka topic
│   ├── kafka_consumer.py      # Consumes and stores data in PostgreSQL
│── sql_queries/
│   ├── metrics.sql            # SQL queries for key business metrics
│── visualizations/
│   ├── tableau_dashboard.twb  # Tableau dashboard file
│── README.md
```
---
## 🛠️ Setup & Installation
### Prerequisites
- Docker
- Python 3
- PostgreSQL
- Apache Kafka
- Tableau Public (for visualization)

---
### Steps to Run
1. **Clone the Repository**
   ```bash
   git clone https://github.com/yourusername/Sales-and-User-Behavior-Analysis.git
   cd Sales-and-User-Behavior-Analysis
   ```

2. **Start Kafka and PostgreSQL Containers**

3. **Generate Synthetic Data**
   ```bash
   python data_generation/generate.py
   ```

4. **Start Data Streaming**
   - **Kafka Producer**
     ```bash
     python data_streaming/kafka_producer.py
     ```
   - **Kafka Consumer**
     ```bash
     python data_streaming/kafka_consumer.py
     ```

5. **Run SQL Queries for Metrics**

6. **Visualize Data with Tableau**

---

## 📊 Key Insights
- **Top-selling products**
- **Daily and monthly sales trends**
- **User purchase frequency**
- **Revenue trends over time**

## 📈 Future Improvements
- Implement data quality checks
- Automate data pipeline using Apache Airflow
- Deploy the entire pipeline to a cloud platform (AWS, GCP, or Azure)

## 👨‍💻 Contributors
- **Sidharth Srinivasan** - [GitHub](https://github.com/SidharthSrinivasan)


