from distutils.core import setup
REQUIRES = [
    'structlog',
    'sqlalchemy',
    'allure-pytest'
]

setup(
    name='orm_client',
    version='0.0.1',
    packages=['orm_client'],
    url='https://github.com/AlexStark9/orm_client.git',
    license='MIT',
    author='Alex Stark',
    author_email='-',
    install_requires=REQUIRES,
    description='orm client with allure and loger'
)
