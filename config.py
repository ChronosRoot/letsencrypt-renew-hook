from configparser import ConfigParser
import os


CONFIG_FILENAME = "config.ini"
configFilepath = (
    os.path.split(os.path.realpath(__file__))[0] + os.path.sep + CONFIG_FILENAME
)
config = ConfigParser()
config.read(configFilepath)
