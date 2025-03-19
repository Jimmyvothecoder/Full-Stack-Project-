# Stock Brokerage System

## Overview

The Stock Brokerage System is a full-stack application that facilitates stock and bond trading for investors. It provides a robust API for managing investors, stocks, bonds, and transactions while enforcing business rules to ensure valid trading operations. This project is designed to simulate a real-world brokerage platform, helping users track their portfolios and execute trades efficiently.

## Features

  * **CRUD Operations:** Manage investors, stocks, bonds, and transactions.

  * **Business Rules Enforcement:** Prevent invalid sales (e.g., selling more shares than owned).

  * **Portfolio Display:** Show an investor's holdings, including current stocks, bonds, and their respective values.

  * **Transaction Management:** Record and process buy/sell orders.

  * **Database Integration:** Uses MySQL for storing and retrieving data efficiently.

## Technologies Used

  * **Backend:** Python (Flask/FastAPI/Django)

  * **Database:** MySQL with ```mysql-connector-python```

  * **Frontend:** EJS 

  * **API Documentation:** Swagger or Postman

  * **Version Control:** Git & GitHub

## Setup Instructions

### Prerequisites

  * Python 3.8+

  * MySQL Server

  * Node.js (if frontend is included)

### Installation Steps

1. **Clone the repository:**

      ```git clone https://github.com/yourusername/stock-brokerage-system.git
      cd stock-brokerage-system

2. **Set up a virtual environment (Optional but recommended):**

      ```python -m venv venv
      source venv/bin/activate  # On Windows use `venv\Scripts\activate`

3. **Install dependencies:**

      ```pip install -r requirements.txt```

4. **Configure MySQL Database:**

   * Create a database named brokerage_db.
      
   * Update database connection settings in config.py.
      
   * Run migrations or execute schema.sql to set up tables.

5. **Run the application:**

      ```python app.py```

6. **Test API Endpoints:**

    * Use Postman or curl to test API routes.
          
    * Example request:
      
          curl -X GET http://localhost:5000/investors

## API Endpoints

### Investors

* Get all investors:

    `GET /investors`

* Get a specific investor:

    `GET /investors/{id}`

* Create a new investor:

    `POST /investors`

* Update an investor:

    `PUT /investors/{id}`

* Delete an investor:

    `DELETE /investors/{id}`



## Future Improvements

  * Implement a web-based frontend with React.js.

  * Introduce real-time stock price updates.

  * Add authentication and authorization features.

  * Integrate machine learning for portfolio recommendations.

## Contributing

  Contributions are welcome! Please submit a pull request or open an issue to discuss improvements.

## Contact

For any inquiries or support, contact Jimmy Vo at [jtvo8@cougarnet.uh.edu](jtvo8@cougarnet.uh.edu).
