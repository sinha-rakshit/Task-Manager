# Task Manager

This Task Manager project, developed as a part of the learning process is a simple command-line application built using Python and MySQL and containerized using Docker. 


## Features

The Task Manager offers the following features:

- Add a new user with user ID, name, and date of birth.
- Add a task for an existing user, including task ID, user ID, task description, and deadline.
- Delete a user, which also deletes all associated tasks.
- Delete a task based on the task ID.
- Update user information, including user ID, name, task, or deadline.
- Search and display tasks for a specific user based on the user ID.

## Technologies Used

The following technologies were used in developing this project:

- ****Python****: The programming language used to write the task manager application.
- ****MySQL****: The database management system used to store user and task data.
- ****MySQL Connector/Python****: The Python library used to establish a connection with the MySQL database.
- ****Docker****: Containerization technology used to package the application and its dependencies.

## Setup and Installation

### Local Installation

To run the Task Manager application locally, follow these steps:

1. Install Python (version 3.9 or higher) and MySQL on your system if they are not already installed.
2. Clone the repository or download the project files.
3. Install the required Python packages by running the following command:
   
   ```bash
    pip install mysql-connector-python
    ```
5. Set up a MySQL database and create the necessary tables using the provided database schema.

#### User_Info Table

| Column Name    | Data Type | Description         |
| -------------- | --------- | ------------------- |
| userID (PK)    | varchar   | User ID (Primary Key)|
| NAME           | varchar   | User name            |
| Date_of_Birth  | date      | User's date of birth |

#### Task Table

| Column Name    | Data Type | Description         |
| -------------- | --------- | ------------------- |
| task_id (PK)   | varchar   | Task ID (Primary Key)|
| user_ID (FK)   | varchar   | User ID (Foreign Key)|
| Task           | varchar   | Task description     |
| Deadline       | date      | Task deadline        |



### Running the Project with Docker

Alternatively, you can run the Task Manager project using Docker. The Dockerfile provided in the project allows you to build a Docker image that includes all the necessary dependencies and project files. 

Follow the steps below to run the project with Docker:

1. Install Docker on your system if it is not already installed.
2. Clone the repository or download the project files.
3. Open a terminal or command prompt and navigate to the project directory containing the Dockerfile.
4. Build the Docker image by running the following command:

    ```bash
    docker build -t task-manager  .
    ```
This command will build the Docker image named `task-manager` using the Dockerfile and project files.

5. After the image is successfully built, run the Docker container using the following command:

   ```bash
    docker run -it --net host task-manager
    ```
   
The `--net host` flag is used to allow the container to access the host network. This is necessary for the container to connect to the MySQL database running on the host machine.





