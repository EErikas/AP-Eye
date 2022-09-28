# ResMon
Resource Monitoring application with API endpoints to start and stop logging system load. Great for testing system loads in specific scenarios

All files are saved to `out` folder in project root directory
## Endpoints
* `/start/<name>`: Starts logging to a file that is called `<name>.csv`
  
  - Response if logging is successful:
    ```json
    {"logging": "started"}
    ```
  - Response if another logging process is ongoing:
    ```json
    {"error": "already running"}
    ```
* `/stop`: Stops logging process, returns response
  ```json
  {"logging": "stopped"}
  ```
* `/serve/<file>`: Downloads log file in csv format or returns error if it was not found
* `/status`: Returns status of the logging process
  -  Response if logging is ongoing:
        ```json
        {"logging": "ongoing"}
        ```
  -  Response if logging status is stopped:
        ```json
        {"logging": "stopped"}
        ```
* `/clean`: Deletes all logs. Logging must be stopped for the operation to work.
    -  Response if logging is ongoing:
        ```json
        {"error": "logging is ongoing"}
        ```
  -  Response if deletion was successful:
        ```json
        {"logging": "logs removed"}
        ```