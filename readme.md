# Containerizer System
This project is a simple platform built with Django for running Docker containers. It includes endpoints for creating, listing, getting, deleting, and editing apps, as well as an endpoint for running apps and creating containers. The platform also keeps a history of docker runs, including the time of execution and parameters used, and allows for editing changes and tracking the status of each execution.

##  Software Requirements Specification Overview
- Create, Run and Stop Containers 
- Track and Record Execuation Status

## System Design
In this web platform developed using Django Rest framework, there are two base use cases, "Authentication" and "Containerization". Each app has its own responsibilties and handles specific operations.

### Authentication
In the platform, Authentication is developed using the Djoser library and Simple JWT utilizes Django's pre-built User model.

By integrating Djoser with Simple JWT, authentication in the web platform utilizes Djoser's built-in functionalities for user registration and login while also leveraging Simple JWT's capabilities for token-based authentication. This combination enables secure authentication mechanisms for RESTful APIs, ensuring that users can authenticate and access the platform's resources using JWTs.

### Containerization
The containerizer app consists of three main models: App, Container and RunningHistoryRecord.

1. App Model:
    The App model represents a Docker image that can be run as a container. It includes fields for the name of the app, the image address, environment variables, and the command to run the app.

2. Container Model:
    The Container model represents a running instance of an app. 
    - `created_at`: This field is a DateTimeField with `auto_now_add=True`.
    - `stopped_at`: This field is a DateTimeField too. These are useful for tracking <ins>running</ins> time of containers.

3. RunningHistoryRecord Model:
    The RunningHistoryRecord model represents a record of a container's execution history. It includes a foreign key to the Container model, a status field to track the status of the execution, environment variables used, and a timestamp for when the execution occurred.
    - `created_at`: This field is a DateTimeField with `auto_now_add=True`. It captures the timestamp when an object is created, indicating the date of new change. This is useful for tracking running history within specific time periods.


## Database and Indexing
The project is using PostgreSQL as the database. Although MySQL is reported to be slightly faster than PostgreSQL in write operations according to recent benchmarks, PostgreSQL was chosen for its high compatibility with the Django framework and better data compatibility.

Additionally, the decision has been made not to use indexing in the database. While indexing can improve performance in read operations and data retrieval, it can potentially slow down write operations. Since the majority of the platform's operations are write-type operations(running history records), the decision has been made to forgo indexing in favor of optimizing write performance.

This approach indicates a prioritization of efficient data writes and a willingness to trade off some read performance. 