#!/usr/bin/env python

from setuptools import setup

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(name='pipelinewise-tap-kafka',
      version='4.1.0',
      description='Singer.io tap for extracting data from Kafka topic - PipelineWise compatible',
      long_description=long_description,
      long_description_content_type='text/markdown',
      author='TransferWise',
      url='https://singer.io',
      classifiers=[
          'License :: OSI Approved :: GNU Affero General Public License v3',
          'Programming Language :: Python :: 3 :: Only'
      ],
      install_requires=[
          'kafka-python==2.0.1',
          'pipelinewise-singer-python==1.*',
          'dpath==2.0.1',
          'filelock==3.0.12',
          'kafkian==0.13.0',
          'requests==2.20.0'
      ],
      extras_require={
          "test": [
              "pytest==5.0.1",
              "nose==1.3.7",
              "pylint==2.4.2"
          ]
      },
      entry_points='''
          [console_scripts]
          tap-kafka=tap_kafka:main
      ''',
      packages=['tap_kafka']
)
