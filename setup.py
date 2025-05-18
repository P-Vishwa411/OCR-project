from setuptools import setup, find_packages

setup(
    name="OCR-project",
    version="0.1.0",
    author="vishwa",
    author_email="chantip050@gmail.com",
    description="A Python project for Optical Character Recognition (OCR)",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/P-Vishwa411/OCR-project.git",
    packages=find_packages(),
    install_requires=[
        "pillow",
        "numpy",
        "opencv-python",
        "pytesseract"
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
)