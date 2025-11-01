
# ETL Sports Data Pipeline

A comprehensive ETL (Extract, Transform, Load) pipeline for processing and analyzing sports player statistics. This project demonstrates data extraction from an API, transformation with pandas, and loading into a MySQL database, with integrated data visualization capabilities.

## 📋 Project Overview

This project implements a complete data engineering workflow that:
- Extracts sports player data from a mock API
- Performs data cleaning and transformation
- Generates aggregated analytics
- Stores processed data in MySQL database
- Visualizes key metrics using matplotlib

## 🎯 Features

- **API Data Extraction**: Fetches sports data from Mockaroo API
- **Data Cleaning**: Handles missing values, duplicates, and data type conversions
- **Feature Engineering**: Creates derived metrics and aggregated statistics
- **Database Integration**: Automated table creation and data loading to MySQL
- **Data Visualization**: Interactive plots for data analysis
- **Export Capabilities**: Saves processed data to CSV files

## 🛠️ Technologies Used

- **Python 3.x**
- **pandas**: Data manipulation and analysis
- **matplotlib**: Data visualization
- **MySQL**: Relational database for data storage
- **mysql-connector-python**: MySQL database connectivity
- **SQLAlchemy**: SQL toolkit and ORM
- **requests**: HTTP library for API calls
- **Jupyter Notebook**: Interactive development environment

## 📁 Project Structure
```
ETL-Sport2/
│
├── scripts/
│   └── data_visualization.ipynb    # Jupyter notebook for visualizations
│
├── data/
│   ├── data.json                   # Raw data from API
│   ├── transformed_data.csv        # Cleaned and transformed data
│   └── filtered_data.csv           # Aggregated data by sport
│
└── README.md                       # Project documentation
```

## 🚀 Getting Started

### Prerequisites
```bash
pip install pandas matplotlib mysql-connector-python sqlalchemy requests jupyter
```

### MySQL Setup

1. Install MySQL Server on your local machine
2. Create a database named `Sport_Db`:
```sql
CREATE DATABASE Sport_Db;
```

### Configuration

Update the following paths in the scripts to match your local environment:
- API endpoint: `https://my.api.mockaroo.com/sport_data.json?key=7dc3b8c0`
- File paths: `C:\Users\P15\Desktop\ETL\data\`
- MySQL credentials: `root:@localhost/Sport_Db`

## 📊 Data Pipeline Workflow

### 1. Data Extraction
```python
# Fetches data from Mockaroo API
url = "https://my.api.mockaroo.com/sport_data.json?key=7dc3b8c0"
response = requests.get(url)
data = response.json()
```

**Output**: Raw JSON data saved to `data.json`

### 2. Data Understanding & Exploration

The pipeline performs comprehensive data analysis:
- Data types and structure inspection
- Summary statistics calculation
- Missing value detection
- Column identification

### 3. Data Cleaning

**Operations performed**:
- **Missing Value Imputation**: Fills missing Goals, Assists, and Points with mean values
- **Duplicate Removal**: Identifies and removes duplicate records
- **Data Type Conversion**: Converts "Matches Won" to numeric format
- **Row Filtering**: Drops rows with remaining null values

### 4. Feature Engineering

**New Features Created**:
- `total_goals`: Calculated as `Games Played × Goals`

**Aggregations**:
- Groups data by Sport
- Calculates sum of Games Played, Goals, and Assists
- Sorts by Goals in ascending order

### 5. Data Export

Two CSV files are generated:
- `transformed_data.csv`: Complete cleaned dataset
- `filtered_data.csv`: Aggregated statistics by sport

### 6. Database Loading

**Table Schema**:
```sql
CREATE TABLE players (
    id INT AUTO_INCREMENT PRIMARY KEY,
    player_name VARCHAR(100) NOT NULL,
    sport VARCHAR(50) NOT NULL,
    team VARCHAR(50) NOT NULL,
    games_played INT,
    goals INT,
    assists INT,
    matches_won INT,
    points INT
);
```

Data is loaded using SQLAlchemy's `to_sql()` method with `replace` strategy.

### 7. Data Visualization

The notebook creates visualizations including:
- Bar chart: Games Played per Sport
- Distribution analysis
- Statistical plots

## 📈 Sample Data Structure

| Column | Type | Description |
|--------|------|-------------|
| player_name | VARCHAR(100) | Name of the player |
| Sport | VARCHAR(50) | Type of sport (Athletics, Football, Tennis, etc.) |
| team | VARCHAR(50) | Team name |
| Games Played | INT | Number of games participated |
| Goals | INT | Total goals scored |
| Assists | INT | Total assists made |
| Matches Won | INT | Number of matches won |
| Points | INT | Total points accumulated |

## 🔍 Key Insights

The pipeline provides:
- Sport-wise performance metrics
- Player statistics aggregation
- Missing data handling strategies
- Scalable database architecture

## 📝 Usage Examples

### Running the ETL Pipeline
```python
# 1. Extract data from API
python extract_data.py

# 2. Clean and transform data
python transform_data.py

# 3. Load data to MySQL
python load_data.py

# 4. Visualize results
jupyter notebook data_visualization.ipynb
```

### Querying the Database
```python
import pandas as pd
from sqlalchemy import create_engine

engine = create_engine("mysql+mysqlconnector://root:@localhost/Sport_Db")
df = pd.read_sql("SELECT * FROM players", con=engine)
print(df.head())
```

## ⚠️ Important Notes

1. **API Key**: The Mockaroo API key is embedded in the code. For production use, store it securely in environment variables.
2. **File Paths**: All file paths are hardcoded for Windows. Update them for your OS.
3. **MySQL Credentials**: Default credentials (root with no password) are used. Update for production environments.
4. **Data Persistence**: Using `if_exists="replace"` will overwrite existing table data.

## 🔧 Troubleshooting

**Connection Issues**:
- Verify MySQL server is running
- Check database credentials
- Ensure `Sport_Db` database exists

**Missing Dependencies**:
```bash
pip install -r requirements.txt
```

**Path Errors**:
- Use raw strings (`r"path"`) or forward slashes in file paths
- Ensure all directories exist before running scripts

## 🚀 Future Enhancements

- [ ] Add data validation layer
- [ ] Implement incremental data loading
- [ ] Create automated scheduling (cron jobs/Airflow)
- [ ] Add error logging and monitoring
- [ ] Build REST API for data access
- [ ] Implement data quality checks
- [ ] Add more visualization dashboards
- [ ] Create unit tests

## 📄 License

This project is for educational and demonstration purposes.

## 👤 Author

**MohamedSAIFI0**
- GitHub: [@MohamedSAIFI0](https://github.com/MohamedSAIFI0)
- Commit: b8e9224 (8 months ago)

## 🤝 Contributing

Contributions, issues, and feature requests are welcome!

---

**Note**: This is a learning project demonstrating ETL principles and data engineering best practices.
