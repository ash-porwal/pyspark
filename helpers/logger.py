class Log4J:
    def __init__(self, spark_session):
        # this is how we can get a JVM object
        log4j = spark_session._jvm.org.apache.log4j

        # making logger attribute
        # in my log4j.properties files, I've define this `ashish.spark.example` as my log name
        # so, we need to pass this above name in our logger to make all this logger config work.
        root_class = "ashish.spark.example"

        # and more in my log name I want to get the application name as well
        # so from sparksession we can get the application name

        conf = spark_session.sparkContext.getConf()

        #once I've the config, then i can query the spark app name
        app_name = conf.get("spark.app.name", "defaultAppName")

        self.logger = log4j.LogManager.getLogger(root_class + "." + app_name)
    
    def warn(self, msg):
        self.logger.warn(msg)

    def info(self, msg):
        self.logger.info(msg)

    def error(self, msg):
        self.logger.error(msg)

    def debug(self, msg):
        self.logger.debug(msg)