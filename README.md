# Credit Exploratory Data Analysis (EDA)
A comprehensive data analytics dashboard and exploratory pipeline for profiling credit applicants, isolating risk behaviors, and analyzing payment defaults using Python, Pandas, Seaborn, and Streamlit.

## Project Structure
```
CreditEDA/
├── data/                        # Datasets & Column Documentation
│   ├── application_data.csv     # Current client loan application records
│   ├── previous_application.csv # Historical loan application records
│   └── columns_description.xlsx # Data dictionary and column definitions
├── src/                         # Core Scripts & Pipeline Code
│   └── Doc3Credit.py            # Original exploratory data analysis script
├── .streamlit/                  # Streamlit Theme & Configuration
├── app.py                       # Main Interactive Streamlit Dashboard Application
└── requirements.txt             # Python Project Dependencies
```

## Features
### 1. Multi-Dataset Ingestion & Inspection
- Loads high-dimensional client application and previous loan contract files into structured Pandas DataFrames
- Automated null value detection and sparsity calculation across features
- Seamless loading from `data/`, current root, or parent directories
- Visual overview of raw dataset dimensions and column data types

### 2. Automated Null Pruning & Statistical Imputation
- Prunes sparse columns with missing entries exceeding the 47% threshold
- Robust median imputation for continuous numeric variables (`AMT_ANNUITY`, `AMT_GOODS_PRICE`, `EXT_SOURCE_2`, `EXT_SOURCE_3`)
- Mode and custom tag imputation for categorical fields (`OCCUPATION_TYPE`, `NAME_TYPE_SUITE`, `CNT_FAM_MEMBERS`)
- Eliminates outlier distortion in baseline risk indicators

### 3. Demographic Standardization & Binning
- Transforms negative relative birth and phone change days into readable absolute age years
- Converts continuous age values into discrete age groups (`Below 25`, `25-45`, `45-65`, `65-85`)
- Categorizes total loan credit amounts into meaningful tiers (`Very Low Credit`, `Low Credit`, `Medium Credit`, `High Credit`, `Very High Credit`)
- Generates demographic pie charts and category distributions

### 4. Univariate, Bivariate & Multivariate Analysis
- Plots single-variable distributions for credit amounts and applicant demographics
- Overlays bivariate density curves comparing goods price distributions between repayers (`TARGET = 0`) and defaulters (`TARGET = 1`)
- Builds Pearson correlation coefficient heatmaps among numeric variables (income, credit, annuity, age)
- Evaluates contract statuses (`Approved`, `Refused`, `Canceled`, `Unused`) across historical applications

### 5. Interactive Code Explorer & Raw Source View
- Interactive 10-block execution console with live progress indicators and dynamic charts
- Explanatory tooltips and technical breakdowns for each step of the pipeline
- Built-in source code viewer to inspect the original `Doc3Credit.py` analytical routine

## Technologies Used
- **Backend & Analytics**: Python 3, Pandas, NumPy
- **Data Visualization**: Seaborn, Matplotlib
- **Web Dashboard**: Streamlit
- **Layout & Styling**: HTML5, CSS3 (Custom Glassmorphic & Responsive UI)

## Setup & Configuration
### Prerequisites
- Python 3.8 or higher
- pip package manager
- Streamlit 1.20+

### Installation Steps
1. **Clone the repository**
   ```bash
   git clone https://github.com/yourusername/CreditEDA.git
   cd CreditEDA
   ```

2. **Install required dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Verify Dataset Placement**
   Ensure that the datasets are located in the `data/` directory (or project root):
   - `data/application_data.csv`
   - `data/previous_application.csv`
   - `data/columns_description.xlsx`

## Building & Running the Project
### Running the Application
Launch the Streamlit dashboard locally:
```bash
streamlit run app.py
```
Access the application in your browser at:
`http://localhost:8501/`

### Executing the Standalone Analysis Script
To run the exploratory data analysis script via the command line:
```bash
python src/Doc3Credit.py
```

## Dashboard Views & Navigation Tabs
### Navigation Menu
- `Project Overview` - Executive abstract, core objectives, 5-stage pipeline workflow, and key metrics ribbon (`49,000+` applications, `1.67M` historical records, `~8.0%` default rate).
- `1. Data Cleaning & Binning` - Code walkthrough and interactive distribution tables for cleaned features and age categories.
- `2. Univariate Analysis` - Visual distribution comparisons of goods prices between non-defaulting and defaulting applicants.
- `3. Bivariate & Multivariate Analysis` - Pearson correlation matrix heatmaps identifying linear dependencies.
- `4. Full Code Explorer` - Step-by-step interactive execution console covering data loading, null handling, binning, target imbalance, and multi-table joins.
- `5. View Raw Source Code` - Complete code viewer for the `Doc3Credit.py` analytical pipeline.

## Dataset Schemas & Key Features
### Application Data (`application_data.csv`)
- `SK_ID_CURR (Primary Key)` - Unique identifier for each loan application
- `TARGET` - Loan default indicator (`0` = Repaid on time, `1` = Defaulted)
- `NAME_CONTRACT_TYPE` - Type of loan contract (`Cash loans`, `Revolving loans`)
- `CODE_GENDER` - Gender of the applicant
- `FLAG_OWN_CAR`, `FLAG_OWN_REALTY` - Ownership flags for assets
- `CNT_CHILDREN` - Number of children the applicant has
- `AMT_INCOME_TOTAL` - Total annual income of the applicant
- `AMT_CREDIT` - Credit amount of the loan
- `AMT_ANNUITY` - Loan annuity amount
- `AMT_GOODS_PRICE` - Price of goods for which the loan is given
- `DAYS_BIRTH`, `YEARS_BIRTH` - Client's age in days and absolute years
- `AGE_Category`, `AMT_CREDIT_Category` - Discretized demographic and financial bins

### Previous Application Data (`previous_application.csv`)
- `SK_ID_PREV (Primary Key)` - Unique ID of previous loan application
- `SK_ID_CURR (Foreign Key)` - ID linking to current application record
- `NAME_CONTRACT_TYPE` - Previous loan product type
- `AMT_ANNUITY`, `AMT_APPLICATION`, `AMT_CREDIT`, `AMT_GOODS_PRICE` - Historical financial figures
- `NAME_CONTRACT_STATUS` - Application outcome (`Approved`, `Refused`, `Canceled`, `Unused`)

## Key Analytical & Statistical Practices
- **Threshold-Based Pruning**: Automatic dropping of features with `>47%` missing values to prevent noisy inferences.
- **Robust Median Imputation**: Eliminates skewness from high-value financial outliers when filling missing numerical cells.
- **Data Binning & Discretization**: Translates continuous distributions into structured categorical buckets for segmentation.
- **Class Imbalance Inspection**: Explicit monitoring of target variable skewness (`~92%` non-defaulters vs. `~8%` defaulters).
- **Relational Joins & Pivot Aggregations**: Merging current and historical data on `SK_ID_CURR` to evaluate past credit behaviors across income streams.

## Future Enhancements
- Integration of predictive machine learning models (XGBoost / Random Forest) for automated default scoring
- Interactive client risk score calculator widget in the sidebar
- Automated downloadable PDF/Excel EDA summary report generation
- Real-time SQL database connector for streaming new loan applications
- Advanced SHAP value explainability charts for individual credit risk assessment

## Troubleshooting
### Dataset File Not Found Error
- **Issue**: `application_data.csv` or `previous_application.csv` not found.
- **Solution**: Ensure the dataset files are placed inside the `data/` directory or in the main project directory. The app checks both automatically.

### Streamlit Port Already in Use
- **Issue**: Port `8501` is occupied by another application.
- **Solution**: Run Streamlit on a custom port using:
  ```bash
  streamlit run app.py --server.port 8502
  ```

### High Memory Usage During Dataset Loading
- **Issue**: System slows down when processing 1.67M+ historical records.
- **Solution**: Ensure your environment has at least 4GB of available RAM, as Streamlit caches data in memory via `@st.cache_resource`.

## Performance Optimization
- **Streamlit Caching**: Utilizes `@st.cache_resource` for instantaneous dataframe loading and preprocessing across user sessions.
- **Vectorized NumPy Operations**: Executes high-speed demographic normalizations and transformations without explicit loops.
- **Selective Column Processing**: Prunes sparse features early in the pipeline to minimize in-memory data footprint.

## License
This project is open source and available under the MIT License.

## Author
Developed by: Noor Mohammad

## Support
For issues and questions, please refer to the documentation or contact support.

## Deployment Checklist
- [x] Main datasets created and placed in `data/` directory
- [x] File loaders in `app.py` and `Doc3Credit.py` configured for dynamic resolution
- [x] Python dependencies documented in `requirements.txt`
- [x] Interactive Streamlit dashboard (`app.py`) tested and running
- [x] Standalone script (`src/Doc3Credit.py`) verified
- [x] All 10 Interactive Code Explorer blocks tested
- [x] Full UI responsiveness verified on Desktop and Mobile viewports
- [x] Zero functionality or UI changes introduced during restructuring
