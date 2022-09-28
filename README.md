# ResMon
Resource Monitoring application with API endpoints to start and stop logging system load. Great for testing system loads in specific scenarios

All files are saved to `out` folder in the project root directory
## Launch methods
There are several ways to launch the application
### From source code
To launch from the source code, make sure you have `Python 3.9` installed and do the following commands:
```bash
pip install -r requirements.txt
python app.py
```
### Using Docker
Official Docker image can be pulled by using this command
```bash
docker pull eerikas/resmon
```
It's best to use `docker compose` for easiest deployments, the example can be seen in the `docker-compose.yml` file.

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
* `/stop`: Stops the logging process, returns the response
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