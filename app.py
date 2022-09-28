from os import path, mkdir, listdir, remove
from csv import writer as csv_writer
from time import sleep
from threading import Thread
from psutil import cpu_percent, virtual_memory, net_io_counters, disk_io_counters
from flask import Flask, jsonify, send_file

ROOT_DIR = path.dirname(path.abspath(__file__))
RESULT_DIR = path.join(ROOT_DIR, 'out')
run_process = False


def write_data(data, filename):
    with open(filename, 'a') as outfile:
        writer = csv_writer(outfile)
        writer.writerow(data)


def log_data(name):
    global run_process
    print(f'-> Logging started at {name}')
    while run_process:
        data = [
            cpu_percent(),
            virtual_memory().percent,
            net_io_counters(pernic=False).bytes_sent,
            net_io_counters(pernic=False).bytes_recv,
            disk_io_counters(perdisk=False).read_count,
            disk_io_counters(perdisk=False).write_count,
            disk_io_counters(perdisk=False).read_bytes,
            disk_io_counters(perdisk=False).write_bytes
        ]
        write_data(data, name)
        sleep(1)
    print('-> Logging completed')


app = Flask(__name__)


@app.route('/start/<string:name>')
def start(name: str):
    global run_process
    if run_process:
        return jsonify(error='already running')
    run_process = True
    if not path.exists(RESULT_DIR):
        mkdir(RESULT_DIR)
    file = path.join(RESULT_DIR, f'{name}.csv')
    if not path.exists(file):
        header = [
            'cpu_usage',
            'ram_usage',
            'network_bytes_sent',
            'network_bytes_recieved',
            'disk_read_count',
            'disk_write_count',
            'disk_read_bytes',
            'disk_write_bytes'
        ]
        write_data(header, file)
    daemon = Thread(target=log_data, args=(file,))
    daemon.start()
    return jsonify(logging='started')


@app.route('/stop')
def stop():
    global run_process
    run_process = False
    return jsonify(logging='stopped')


@app.route('/serve/<string:file>')
def serve_csv(file: str):
    file = path.join(RESULT_DIR, f'{file}.csv')
    if not path.exists(file):
        return jsonify(error='Entry does not exist')
    return send_file(file)


@app.route('/status')
def status():
    global run_process
    return jsonify(logging='ongoing' if run_process else 'stopped')


@app.route('/clean')
def clean():
    global run_process
    if run_process:
        return jsonify(error='logging is ongoing')
    files = [path.join(RESULT_DIR,f) for f in listdir(RESULT_DIR)]
    for file in [f for f in files if path.isfile(f)]:
        remove(file)
    return jsonify(logging='logs removed')


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
