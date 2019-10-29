from setuptools import setup

setup(
    name='msglite',
    version='0.25.0',
    description="Extracts emails and attachments saved in Microsoft Outlook's .msg files",  # noqa
    url='https://github.com/alephdata/msglite',
    author='Originally: Matthew Walker & The Elemental of Creation',
    license='GPL',
    packages=['msglite'],
    py_modules=['msglite'],
    include_package_data=True,
    install_requires=[
        'olefile>=0.46',
        'chardet',
        'pytz',
    ],
)
