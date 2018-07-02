import logging
import os
import time


def main():
    run()


def run():
    setup_logging()
    try:
        ping, download, upload = get_speed_test_results()
    except ValueError as err:
        logging.info(err)
    else:
        logging.info("%5.1f %5.1f %5.1f", ping, download, upload)


def setup_logging():
    log_file = 'speedtest_{}.log'.format(time.strftime('%Y%m%d'))
    logging.basicConfig(
        filename=log_file,
        level=logging.INFO,
        format="%(asctime)s %(message)s",
        datefmt="%Y-%m-%d %H:%M"
    )


def get_speed_test_results():
    ping = download = upload = None

    with os.popen('speedtest-cli --simple') as speedtestOutput:

        for line in speedtestOutput:
            print(line)
            label, value, init = line.split()

            if 'Ping' in label:
                ping = float(value)
            elif 'Download' in label:
                download = float(value)
            elif 'Upload' in label:
                upload = float(value)

    if all((ping, download, upload)):
        return ping, download,  upload
    else:
        raise ValueError("TEST FAILED")


if __name__ == '__main__':
    main()
