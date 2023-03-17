# Past Paper Downloader

This is a Python script to download past exam papers from the [GCE Guide](https://papers.gceguide.com/A%20Levels/) for [A-Levels](https://www.cambridgeinternational.org/programmes-and-qualifications/cambridge-advanced/cambridge-international-as-and-a-levels/) of the Cambridege University. The script automatically downloads past papers for given years and subjects.


## Table of Contents

- [Requirements](#requirements)
- [Install](#install)
- [Usage](#usage)
- [Arguments](#arguments)
- [Examples](#examples)
- [Output](#output)
- [Notes](#notes)

## Requirements
* pymsgbox
* beautifulsoup4
* requests
* argparse
* os
* termcolor
* pygame

 ```
 pip install -r requirements.txt
 ```


## Install

To use this script, follow these steps:

1. Clone the repository or download the `past_paper_downloader.py` file.
2. Download requirements from `requirements.txt`
 ```
 pip install -r requirements.txt
 ```
3. Open a terminal and navigate to the directory containing the file.
4. Run the script using the command `python past_paper_downloader.py`.
5. Follow the prompts to select the year and faculty for which you want to download past papers.
6. The script will download all available past papers for the selected year and faculty and save them in a folder named `Past Papers` in the directory Documents.

## Usage
```py
python past_paper_downloder.py [-h] -s SUBJECT -y YEAR [-pt PAPER_TYPE]
```

## Arguments

* `-h`, `--help` - show help message and exit
* `-s SUBJECT`, `--subject SUBJECT` - the subject for which past papers are to be downloaded
* `-y YEAR`, `--year YEAR` - the year for which past papers are to be downloaded. Can either be a single year or a range of years separated by a hyphen (e.g. `2010-2015`).
* `-pt PAPER_TYPE`, `--paper_type PAPER_TYPE` - optional argument to specify the type of paper to download (e.g. `ms,qp,sf`). Leave empty to download all types.

## Examples

To download past papers for Physics for the year 2022, run the following command:
```py
python past_paper_downloder.py -s Physics -y 2022
```
To download only paper type `qp` and `ms` for Maths for the year 2015, run the following command:
```py
python past_paper_downloder.py -s Maths -y 2015 -pt qp,ms
```
To download all past papers for all subjects for the years 2020-2022:
```py
python download_past_papers.py -s "*" -y 2020-2022
```

## Output
The script will create a directory named "PastPapers" in your Documents directory. Inside this directory, there will be a directory for each subject, and inside each subject directory there will be a directory for each year. Inside each year directory, there will be directories for each paper type (e.g. "qp" for question papers, "ms" for mark schemes). The past papers will be downloaded into the appropriate paper type directory.

## Notes
- The script may take some time to download all the past papers, depending on the number and size of the files.
- The downloaded files will be saved in ~/Documents/PastPapers directory.
- The program will play a notification sound once the downloads are complete.
- The program will display a pop-up message once the downloads are complete.
- If you have any issues or questions about using the script, please open an issue on the GitHub repository.
