# Simple Banking App (Version2)
## CSEC 322 - Web Application Security (Final Project)
*Date: May 25, 2025*

📺 **Project Presentation Video**: [Watch on YouTube](#)

### Live Demo

The application is deployed and accessible online through pythonanywhere.com:

**[#](#)**

---

## Group Members
- Divino Franco R. Aurellano
- Maica S. Romaraog
- Lj Tan T. Saldivar

---


## Introduction
Simple Banking App is a Flask-based web application designed to simulate a basic banking system. This application provides users with the ability to manage accounts, transfer funds, and perform basic banking operations in a secure environment.

## Objectives
1. Develop a comprehensive web-based banking application with robust security measures
2. Implement essential banking features with appropriate security controls
3. Identify and remediate common web application security vulnerabilities
4. Enhance user experience with security-focused feedback and notifications
5. Deploy a secure application to a cloud hosting platform (PythonAnywhere)
6. Document security improvements and provide comprehensive setup instructions

## e. Original Application Features

1. **User Authentication**
   - Login with username/password
   - Registration of new users
   - Password recovery mechanism (email-based)

2. **Account Management**
   - Display of account balance
   - View of transaction history (last 10 transactions)

3. **Fund Transfer**
   - Transfer money to other registered users
   - Confirmation screen before completing transfers
   - Transaction history updated after transfers

4. **User Role Management**
   - Regular user accounts
   - Admin users with account approval capabilities
   - Manager users who can manage admin accounts

5. **Location Data Integration**
   - Philippine Standard Geographic Code (PSGC) API integration
   - Hierarchical location data selection (Region, Province, City, Barangay)

## f. Security Assessment Findings: Vulnerabilities Identified in the Original Application

Despite the following security measures already in place:
- Password hashing with bcrypt
- CSRF protection on forms
- Rate limiting to prevent abuse
- Secure session management
- Two-step transaction confirmation
- Admin approval workflow for new accounts

The initial application still has several security vulnerabilities that need to be addressed:

1. **Password Security Issues**
   - Insufficient password complexity requirements
   - Inadequate protection against password brute force attacks
   - No password expiration policy or account lockout mechanism

2. **Session Management Vulnerabilities**
   - Inadequate session timeout settings
   - Lack of protection against session fixation attacks
   - No prevention of browser back button access to protected content

3. **Authentication and Authorization Weaknesses**
   - Insufficient role-based access control
   - Vulnerable to URL manipulation attacks(bug in RBAC)
   - Missing CSRF protection on critical forms
   - No rate limiting for sensitive endpoints

4. **User Input Validation**
   - Inadequate validation of form inputs
   - No protection against XSS attacks
   - Insufficient error handling

5. **UX and Security Balance**
   - Lack of clear validation error messages
   - No confirmation for critical actions
   - Insufficient feedback for security events

## g. Initial Technology Stack
- **Backend**: Python with Flask framework
- **Database**: MySQL with SQLAlchemy ORM
- **Frontend**: HTML, CSS, Bootstrap 5
- **Authentication**: Flask-Login, Flask-Bcrypt
- **Security**: Flask-Limiter, CSRF protection
- **Forms**: Flask-WTF

## h. Penetration Testing Report: Summary of Vulnerabilities Identified, Exploitation Steps, and Recommendations

We used Burp Suite, a professional web vulnerability testing tool that includes essential features such as Proxy, Repeater, Intruder, and Decoder, which allowed us to intercept, modify, and analyze HTTP requests. In our test, we assessed a target website by capturing user login credentials through the Intercept feature and forwarding the request to Repeater, where we attempted to manipulate the username, password, user role, and session token. Our exploitation attempts were successful; we were able to get the users' credentials due to the system failure to hash it. Aside from that, we also made penetration test using developer tool in web and below are some of the results: 


### 1. Password Security Vulnerabilities

**Vulnerability**: Weak password requirements and validation
- **Exploitation Steps**: 
  1. Created accounts with simple passwords like "password123" that passed validation
  2. Used common password lists to successfully brute force multiple accounts
  3. Observed that password complexity was not enforced

**Recommendations**:
- Implement strict password complexity requirements (minimum length, character diversity)
- Add password strength meters on registration forms
- Implement account lockout after multiple failed attempts

### 2. Session Management Vulnerabilities

**Vulnerability**: Insufficient session security
- **Exploitation Steps**:
  1. Captured session cookies and reused them after extended periods
  2. Successfully accessed authenticated pages using browser back button after logout
  3. Demonstrated session fixation by setting a known session ID before login

**Recommendations**:
- Implement proper session timeout settings
- Use secure, HttpOnly, and SameSite cookie attributes
- Regenerate session IDs on authentication state changes
- Add cache control headers to prevent browser caching of sensitive pages

### 3. CSRF Vulnerabilities

**Vulnerability**: Missing CSRF protection on critical forms
- **Exploitation Steps**:
  1. Created a malicious website that submitted forms to the banking application
  2. Successfully performed fund transfers without user knowledge
  3. Modified user account details through cross-site requests

**Recommendations**:
- Implement CSRF tokens on all forms, especially for sensitive operations
- Add SameSite cookie restrictions
- Implement proper referrer checking

### 4. Input Validation and XSS Vulnerabilities

**Vulnerability**: Inadequate input validation allowing XSS attacks
- **Exploitation Steps**:
  1. Injected JavaScript into form fields that were displayed to other users
  2. Stole session cookies through injected JavaScript

**Recommendations**:
- Implement strict input validation for all user inputs
- Use proper output encoding when displaying user-provided data

### 5. Rate Limiting Vulnerabilities

**Vulnerability**: Lack of rate limiting on sensitive endpoints
- **Exploitation Steps**:
  1. Used automated tools to perform thousands of login attempts per minute
  2. Attempted large numbers of transfers to identify valid account numbers
  3. Overwhelmed server resources with repeated requests

**Recommendations**:
- Implement rate limiting on all sensitive endpoints
- Add progressive delays for repeated failed attempts
- Implement IP-based throttling for suspicious activity

## i. Remediation Plan: Steps Taken to Address Identified Vulnerabilities

### 1. Password Security Enhancements

**Implemented Solutions**:
- Enhanced password validation requiring at least 8 characters and 3 character types (lowercase, uppercase, digits, special characters)
- Added server-side password strength validation in registration and password reset forms
- Implemented bcrypt password hashing with appropriate work factors for secure storage
- Added client-side password strength indicators for real-time feedback

**Code Changes**:
- Added complexity validation in `forms.py` for the `RegistrationForm` class
- Enhanced password hashing mechanism in `models.py` using bcrypt
- Improved error messages for password validation failures

### 2. Session Security Improvements

**Implemented Solutions**:
- Set session timeout to 30 minutes of inactivity
- Implemented secure session cookies with HttpOnly, Secure, and SameSite attributes
- Added session regeneration on login, logout, and privilege changes
- Implemented cache control headers to prevent browser caching of sensitive data

**Code Changes**:
- Updated session configuration in `app.py` to include security settings
- Added cache control headers in global after_request handler
- Implemented session regeneration in authentication-related routes

### 3. CSRF Protection Implementation

**Implemented Solutions**:
- Added CSRF protection to all forms using Flask-WTF
- Implemented proper token validation on form submission
- Added global CSRF protection with CSRFProtect extension

**Code Changes**:
- Initialized CSRF protection in `app.py`
- Added hidden CSRF token fields to all form templates
- Implemented proper error handling for CSRF validation failures

### 4. Input Validation and XSS Prevention

**Implemented Solutions**:
- Added comprehensive input validation for all user inputs
- Implemented proper output encoding in templates
- Added more specific error messages for validation failures

**Code Changes**:
- Enhanced form validators in `forms.py` with more specific requirements
- Improved error handling and user feedback for validation failures
- Added regex-based validation for critical fields

### 5. Rate Limiting Implementation

**Implemented Solutions**:
- Added rate limiting on all sensitive endpoints using Flask-Limiter
- Implemented different rate limits based on endpoint sensitivity
- Added support for Redis as a rate limit storage backend
- Implemented proper error handling for rate limit exceeded scenarios

**Code Changes**:
- Configured Flask-Limiter in `extensions.py`
- Added route-specific rate limits in `routes.py`
- Created a dedicated rate limit error template

### 6. UI/UX Security Improvements

**Implemented Solutions**:
- Added clear, color-coded validation error messages
- Implemented auto-dismissing alerts for security events
- Added confirmation dialogs for critical actions
- Improved user feedback for security-related events

**Code Changes**:
- Enhanced the base template with improved error handling
- Added JavaScript for security confirmations
- Implemented a neumorphic design language for better visual feedback

## j. Technology Stack: Updated List of Technologies Used

### Backend
- **Python 3.7+**: Core programming language
- **Flask**: Web framework for building the application
- **Flask-SQLAlchemy**: ORM for database interactions
- **Flask-Login**: User authentication management
- **Flask-Bcrypt**: Secure password hashing
- **Flask-WTF**: Form handling and CSRF protection
- **Flask-Limiter**: Rate limiting to prevent abuse
- **itsdangerous**: Secure token generation for password reset
- **PyMySQL**: MySQL database connector
- **python-dotenv**: Environment variable management

### Database
- **MySQL/MariaDB**: Relational database for data storage
- **SQLAlchemy ORM**: Object-relational mapping for database interactions

### Frontend
- **HTML5/CSS3**: Core web technologies
- **Bootstrap 5**: Frontend framework for responsive design
- **Neumorphic Design**: Custom CSS design system for a modern UI
- **JavaScript**: Client-side interactivity and validation
- **Bootstrap Icons**: Icon library for visual elements

### Security Tools
- **CSRF Protection**: Preventing cross-site request forgery
- **Bcrypt**: Secure password hashing algorithm
- **Rate Limiting**: Protection against brute force and DoS attacks
- **Session Management**: Secure handling of user sessions
- **Content Security Policy**: Protection against XSS attacks

### External APIs
- **PSGC API**: Philippine Standard Geographic Code API for location data
- **Fallback mechanisms**: For handling external API unavailability

### Deployment
- **PythonAnywhere**: Web hosting platform
- **MySQL Database (hosted)**: Database service
- **WSGI**: Web server gateway interface for deployment

## k. Setup Instructions: Instructions on How to Set Up and Run the Improved Application

### Prerequisites
- Python 3.7 or higher
- pip (Python package manager)
- MySQL Server 5.7+ or MariaDB 10.2+
- Git (for cloning the repository)

### Local Development Setup

1. **Clone the Repository**
   ```powershell
   git clone https://github.com/yourusername/simple-banking-app-v2.git
   cd simple-banking-app-v2
   ```

2. **Create a Virtual Environment** (Optional but recommended)
   ```powershell
   python -m venv venv
   .\venv\Scripts\Activate.ps1
   ```

3. **Install Dependencies**
   ```powershell
   pip install -r requirements.txt
   ```

4. **Configure Environment Variables**
   - Create a `.env` file in the project root with the following variables:
   ```
   MYSQL_USER=your_mysql_username
   MYSQL_PASSWORD=your_mysql_password
   MYSQL_HOST=localhost
   MYSQL_PORT=3306
   MYSQL_DATABASE=simple_banking
   REDIS_URL=memory://  # Use Redis URL if available
   FLASK_DEBUG=FALSE
   ```

5. **Initialize the Database**
   ```powershell
   python init_db.py
   ```

6. **Run the Application**
   ```powershell
   python app.py
   ```

7. **Access the Application**
   - Open your browser and navigate to `http://localhost:5000`
   - Default admin credentials: Username: `admin`, Password: `admin123`

## Future Improvements
- Implement advanced security features such as multi-factor authentication (MFA)
- Add transaction limits and alerts for suspicious activities

## License
This project is licensed under the MIT License.
