# WebsiteMonitor
This project is a website monitoring and alert system developed in Python using the Flask framework. It allows users to monitor the availability of a specified website, automatically sending email notifications when the website is inaccessible or encounters errors.

The project is structured with a main application script (main.py) that initializes the Flask application and starts the scheduler. A configuration script (config.py) specifies key variables for the application.

The data models (models.py) define the structure of the Website, Notification, and User objects, which are stored in a database managed by SQLAlchemy.

The scheduler script (scheduler.py) uses APScheduler to set up periodic tasks that check the availability of each website.

The utility functions (utils.py) assist in tasks such as website checks and email sending.

Finally, the views script (views.py) handles the Flask routes and views for the user interface, including the routes for adding, editing, and deleting websites, as well as viewing the history of checks and notifications, and configuring email settings.

The system design is centered around providing a user-friendly interface for users to easily monitor their websites and receive timely notifications. The API spec and tasks outline the implementation details and dependencies of each module.
