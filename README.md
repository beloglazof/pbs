# Python Basic Auth Server

## Description

Simple web server on Python 3.5 with:
* GET
* CGI
* Basic Authentication

## Install

```
$ pip3 install pbas
```

## Usage

### Start server:

```
$ python3 -m pbas 8000
```

### Basic Auth:

```
$ python3 -m pbas 8000 user:password
```

### For CGI scripts:
* Create `cgi-bin` folder 
* Put your scripts in this folder
* Run on server