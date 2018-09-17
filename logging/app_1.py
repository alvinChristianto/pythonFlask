import logging
#import datetime

#now = datetime.datetime.now()
#timenow=str(now)

#def doingThing():
#    logging.warning('TIME_YEAR => %s' %timenow )

#angka = 3*3
#def my_function():
#    return angka

#print(my_function())

#create LOGGER
app_logger = logging.getLogger('app1')

class getTime:
    def __init__(self):
        self.logger = logging.getLogger('init getTime')
        self.logger.info('creating init instance of getTime')

    def getTimeThing(self):
        self.logger.info('Crafting getTime')
       # now = datetime.datetime.now()
       # timenow=str(now)
        a= 1+1
        #self.logger.info('TIME_YEAR => %s' %timenow )
        self.logger.info('Done Crafting')

def some_function():
    app_logger.info('received a call to "some_function"')
