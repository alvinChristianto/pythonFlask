import logging
import datetime

now = datetime.datetime.now()
timenow = str(now)

def doingThing() :
    logging.warning('TIME YEAR => %s' %timenow )

print(doingThing())
