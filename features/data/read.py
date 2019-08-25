import yaml


class GetEnvironmentInfo ():
    "Get the Browser Type, Driver, App URL and Test Environment"
    with open("config/test_config.yml", 'r') as test_config:
        test_parse = yaml.load(test_config, Loader=yaml.FullLoader)
        TEST_BROWSER = test_parse['browser']
        TEST_ENV = test_parse['environment']

        with open("config/global.yml", 'r') as global_config:
            global_parse = yaml.load(global_config, Loader=yaml.FullLoader)
            GLOBAL_DRIVER = global_parse['driver'][TEST_BROWSER.lower()+'-driver']
            GLOBAL_URL = global_parse[TEST_ENV.lower()]['url']


class GetLoginInfo ():
    "Get login information from YML"

    with open("config/global.yml", 'r') as global_config:
        global_parse = yaml.load(global_config, Loader=yaml.FullLoader)
        GLOBAL_USERNAME = global_parse[GetEnvironmentInfo.TEST_ENV.lower()]['username']
        GLOBAL_PASSWORD = global_parse[GetEnvironmentInfo.TEST_ENV.lower()]['password']
