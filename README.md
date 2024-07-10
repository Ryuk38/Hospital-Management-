# Hospital Management System

The Hospital Management System is a Python-based application for managing patient, doctor, and ambulance service data within a hospital environment. It utilizes MySQL for database management and provides functionalities for CRUD operations on patient and doctor details, as well as ambulance service booking and management.

## Features

- **Patient Management:** Add, update, delete, and print patient details.
  
- **Doctor Management:** Add, update, delete, and print doctor details.
  
- **Ambulance Service:** Book ambulance services, check booking details.
  
- **Security:** Password-protected access to administrative functions.

## Setup Instructions

### Prerequisites

- Python 3.x
- MySQL server

### Installation

1. **Clone the repository:**

   ```bash
   git clone https://github.com/your-username/hospital-management.git
   cd hospital-management
   ```

2. **Install required Python packages:**

   ```bash
   pip install -r requirements.txt
   ```

3. **Set up the database:**

   - Create a MySQL database named `hospital_management`.
   - Import the schema from `database_schema.sql` to create necessary tables.

4. **Configure database connection:**

   - Update `config.py` with your MySQL server credentials.

## Usage

1. **Run the application:**

   ```bash
   python main.py
   ```

2. **Follow the on-screen prompts to manage patients, doctors, and ambulance services.**

## Database Schema

The MySQL database schema includes the following tables:

- `PATIENT_DETAILS`
- `DOCTOR_DETAILS`
- `AMBULANCE_DETAILS`
- `DRIVER_DETAILS`
- `AMBULANCE_SERVICE`

Refer to `database_schema.sql` for schema details.

## Project Structure

```
hospital-management/
│
├── main.py
├── config.py
├── database_schema.sql
├── README.md
├── requirements.txt
└── ...
```

## Contributing

Contributions are welcome! Please submit any bug fixes or improvements via pull requests.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

