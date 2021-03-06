#!/usr/bin/env python3
from setuptools import setup


PLUGIN_ENTRY_POINT = 'guiplayer=plugin_playback_guiplayer'

setup(
    name='plugin_playback_guiplayer',
    version='0.0.1a1',
    description='GUI Player Plugin For Mycroft Audio Service',
    url='https://github.com/MycroftAI/plugin-playback-gui-player',
    author='aiix',
    author_email='aix.m@outlook.com',
    license='Apache-2.0',
    packages=['plugin_playback_guiplayer'],
    zip_safe=True,
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Topic :: Text Processing :: Linguistic',
        'License :: OSI Approved :: Apache Software License',

        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.0',
        'Programming Language :: Python :: 3.1',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
    ],
    keywords='playback gui player audio plugin',
    entry_points={'mycroft.plugin.audioservice': PLUGIN_ENTRY_POINT}
)
