<a name="top"/>

Termhub in 5 Minutes: python Tutorial
===================================================

This tutorial shows how to use Python programming language to access content from the TermHub Terminology API.
All the operations describes here perform a GET request.

Prerequisites
-------------

* Python 3.7+

* All libraries in 'requirements.txt' must be installed.
    * Run the command 'pip install -r requirements.txt' in a console window to check these libraries and install any
      that are not already installed.
    * If pip itself is not installed, run the command 'curl <https://bootstrap.pypa.io/get-pip.py> -o get-pip.py; python
      get-pip.py' to install it.

The various scripts make use of the `python-examples/config.ini` file to load necessary information that is uniform
across all tests.

Sample Python Calls
-----------------

The following examples are exhibited by various unit tests defined in the code in `python-examples`.
All commands to run these tests should be run from that directory.

- [login ](#login)
- [get-terminologies](#get-terminologies)
- [get-terminology](#get-terminology)
- [get-concept](#get-concept)
- [get-concept-relationships](#get-concept-relationships)
- [get-concept-treepos](#get-concept-treepos)
- [find-concepts](#find-concepts)

## Login

Log into TermHub via username and password

Command: `TODO:enter command here`

```{.python}
TODO: FILL CODE HERE
```

[Back to Top](#termhub-in-5-minutes-python-tutorial)

## Get Terminologies

Return all loaded terminologies currently hosted by the API.

Command: `TODO:enter command here`

```{.python}
TODO: FILL CODE HERE
```

[Back to Top](#termhub-in-5-minutes-python-tutorial)

## Get Terminology

Return the specific terminology for the abbreviation, publisher, and version.

Command: `TODO:enter command here`

```{.python}
TODO: FILL CODE HERE
```

[Back to Top](#termhub-in-5-minutes-python-tutorial)

## Get Concept

Return summary concept information for a given terminology and code. The following
example gets the 73211009 | Diabetes mellitus | concept in SNOMEDCT.

Command: `TODO:enter command here`

```{.python}
TODO: FILL CODE HERE
```

[Back to Top](#termhub-in-5-minutes-python-tutorial)

## Get Concept Relationships

Return concept relationship information for a given terminology and code. The
following example finds relationships for the 73211009 | Diabetes mellitus | concept in
SNOMEDCT_US. It limits the results to 5 entries and sorts by the "additionalType"
field.

Command: `TODO:enter command here`

```{.python}
TODO: FILL CODE HERE
```

[Back to Top](#termhub-in-5-minutes-python-tutorial)

## Get Concept Treepos

Return concept relationship information for a given terminology and code. The
following example finds relationships for the 73211009 | Diabetes mellitus | concept in
SNOMEDCT. It limits the results to 5 entries and sorts by the "additionalType"
field.

Command: `TODO:enter command here`

```{.python}
TODO: FILL CODE HERE
```

[Back to Top](#termhub-in-5-minutes-python-tutorial)

## Find Concepts

Used to perform text searches to find matching concepts. The following example
performs a text search for "diabetes mellitus" and limits search results to 5
entries.

Command: `TODO:enter command here`

```{.python}
TODO: FILL CODE HERE
```

[Back to Top](#termhub-in-5-minutes-python-tutorial)

