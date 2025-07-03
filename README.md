# Finance Portfolio Tracker

A web-based stock portfolio management application built with Flask that allows users to simulate buying and selling stocks using real-time stock data.

## Features

- **User Authentication**: Secure user registration and login system with password hashing
- **Stock Portfolio Management**: 
  - View current portfolio with real-time stock prices
  - Track total portfolio value and cash balance
- **Stock Trading Simulation**:
  - Buy stocks with virtual cash
  - Sell owned stocks
  - Real-time stock price lookup using external API
- **Transaction History**: Complete record of all buy/sell transactions
- **Stock Quotes**: Look up current stock prices and company information

## Technology Stack

- **Backend**: Python Flask
- **Database**: SQLite with CS50 SQL library
- **Frontend**: HTML/CSS with Jinja2 templating
- **Session Management**: Flask-Session with filesystem storage
- **Stock Data**: Real-time stock prices via CS50 Finance API
- **Security**: Werkzeug password hashing

## Project Structure

```
finance-project/
├── app.py                 # Main Flask application
├── helpers.py            # Helper functions (authentication, stock lookup, formatting)
├── finance.db           # SQLite database
├── requirements.txt     # Python dependencies
├── templates/           # HTML templates
│   ├── layout.html      # Base template
│   ├── index.html       # Portfolio dashboard
│   ├── buy.html         # Stock purchase form
│   ├── sell.html        # Stock selling form
│   ├── quote.html       # Stock quote lookup
│   ├── history.html     # Transaction history
│   ├── login.html       # User login form
│   ├── register.html    # User registration form
│   └── apology.html     # Error message template
├── static/              # Static assets
│   ├── styles.css       # Application styles
│   └── favicon.ico      # Site icon
└── flask_session/       # Session storage directory
```

## Installation

1. **Clone or download the project files**

2. **Install Python dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Set up the database**:
   The application uses SQLite with the following tables:
   - `users`: Store user accounts (id, username, password hash, cash balance)
   - `transactions`: Store all stock transactions (user_id, symbol, shares, price, timestamp)

## Usage

1. **Start the application**:
   ```bash
   python app.py
   ```

2. **Access the application**:
   Open your web browser and navigate to `http://127.0.0.1:5000`

3. **Register a new account**:
   - Click "Register" to create a new user account
   - Choose a unique username and secure password
   - New users start with $10,000 in virtual cash

4. **Use the application**:
   - **Portfolio**: View your current stock holdings and cash balance
   - **Quote**: Look up current stock prices
   - **Buy**: Purchase stocks using your available cash
   - **Sell**: Sell stocks you currently own
   - **History**: View all your past transactions

## Routes

- `GET/POST /` - Portfolio dashboard (login required)
- `GET/POST /register` - User registration
- `GET/POST /login` - User login
- `GET /logout` - User logout
- `GET/POST /quote` - Stock price lookup (login required)
- `GET/POST /buy` - Buy stocks (login required)
- `GET/POST /sell` - Sell stocks (login required)
- `GET /history` - Transaction history (login required)

## Key Functions

### helpers.py
- `lookup(symbol)`: Fetches real-time stock data from CS50 Finance API
- `usd(value)`: Formats numbers as USD currency
- `apology(message, code)`: Renders error messages
- `login_required`: Decorator to protect routes requiring authentication

### Database Schema
- **users table**: id, username, hash, cash
- **transactions table**: id, user_id, symbol, shares, price, timestamp

## Security Features

- Password hashing using Werkzeug's security functions
- Session-based authentication
- Input validation and sanitization
- CSRF protection through proper form handling
- Login required decorators for protected routes

## API Integration

The application integrates with CS50's Finance API (https://finance.cs50.io/) to fetch real-time stock data including:
- Current stock prices
- Company names
- Stock symbols

## Error Handling

The application includes comprehensive error handling for:
- Invalid stock symbols
- Insufficient funds for purchases
- Attempting to sell more shares than owned
- Missing or invalid form inputs
- Network errors during API calls

## Development Notes

- Debug mode is enabled in the main application
- Sessions are stored in the filesystem for persistence
- The application includes cache control headers to prevent caching issues
- Flash messages provide user feedback for successful operations

## Future Enhancements

Potential improvements could include:
- Real-time portfolio updates
- Stock charts and historical data
- Watchlist functionality
- Portfolio performance analytics
- Mobile-responsive design improvements
- Additional stock market data sources

## License

This project is for educational purposes and portfolio demonstration.
