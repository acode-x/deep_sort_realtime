from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="deep-sort-realtime",
    version="1.3.2",
    author="levan92",
    author_email="lingevan0208@gmail.com",
    description="A more realtime adaptation of Deep SORT",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/levan92/deep_sort_realtime",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    packages=find_packages(exclude=("test",)),
    install_requires=[
        "numpy",
        "scipy",
        "opencv-python-headless",
    ],
)
