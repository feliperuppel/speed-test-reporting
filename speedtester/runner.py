import speedtester.logger as logger
import time

# 60 sec times 60 minutes
ONE_HOUR = 60 * 60


def start():
    print("Starting monitoring: {} ".format(time.strftime("%d/%m/%Y - %H:%M:%S")))
    while True:
        print("Executing test\n")
        logger.run()
        print("Sleeping for {} seconds".format(ONE_HOUR))
        time.sleep(ONE_HOUR)


if __name__ == '__main__':
    start()

