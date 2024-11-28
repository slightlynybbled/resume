# Purpose

To control the files and build utilities used to create the basic resume.

To see the results of the build, checkout the [html version of the resume](https://slightlynybbledresume.readthedocs.io/en/latest/)!

Additional purpose of this repository is to exhibit some degree of knowledge of:

 * [Markdown](https://commonmark.org/)
 * [Git](https://git-scm.com/)
 * [GitHub](https://github.com)
 * [ReadTheDocs](https://about.readthedocs.com/?ref=readthedocs.com)
 * [Sphinx](https://www.sphinx-doc.org/en/master/)

## Setup

I like to use [uv](https://docs.astral.sh/uv/) to manage my build environments lately, so I will clone the repository then sync the environment.

```bash
git clone git@github.com:slightlynybbled/resume.git
```

```bash
uv sync
```

## Building the Resume

The `uv` package doesn't appear to like the `make.bat` file, so I will activate the virtual environment before continuing:

```bash
.venv\Scripts\activate.bat
```

To make a normal HTML page with full navigation:

```bash
make html
```

To make a single-page version:

```bash
make singlehtml
```

To make a pdf version:

```bash
make latexpdf
```
