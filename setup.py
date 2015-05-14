from setuptools import setup, find_packages
from pip.req import parse_requirements

install_reqs = parse_requirements("./requirements.txt")
reqs = [str(ir.req) for ir in install_reqs]
print(reqs)

setup(
    name="offyt",
    version="0.1",
    packages=find_packages(),
    scripts=['offyt.py'],

    install_requires=reqs,

    author="Koen Bollen",
    author_email="meneer@koenbollen.nl",
    description="Offline YouTube Playlist Synchronization",
    license="ISC",
    keywords="youtube offline playlist synchronization download",
    url="https://github.com/koenbollen/offyt"
)
