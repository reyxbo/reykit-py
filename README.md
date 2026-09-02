[中文](README_zh.md)

# reykit

**reykit** is a Python general-purpose utility method integration package.

It provides commonly used utility methods for data processing, network requests, file operations, image processing, logging, random values, regular expressions, scheduled tasks, system operations, table processing, multitasking, text processing, time processing, decorators, and more.

It also provides functional modules for DLL files, e-mail, standard input and output, and integrates commonly used Python development utilities through a modular design, reducing the need to repeatedly implement basic utility functions.

It is suitable for general-purpose utility method calls and basic functionality integration in Python application development.

## Features

* Provides a wide range of general-purpose Python utility methods
* Modular design, allowing different functionalities to be used as needed
* Provides unified method exports
* Provides Python basic data type processing methods
* Provides encoding and decoding methods such as JWT and bcrypt
* Provides e-mail sending and content processing methods
* Provides image compression, QR code, and CAPTCHA processing methods
* Provides application logging and runtime data storage methods
* Provides HTTP, URL, Cookie, Socket, and other network processing methods
* Provides file, folder, and temporary file processing methods
* Provides random value and random data processing methods
* Provides regular expression processing methods
* Provides database-integrated scheduled task methods
* Provides standard input/output and terminal printing methods
* Provides operating system, process, memory, and environment related methods
* Provides table data conversion and processing methods
* Provides multitasking methods for threads and coroutines
* Provides text and string processing methods
* Provides time processing and execution time measurement methods
* Provides a wide range of decorator methods
* Provides Windows DLL file injection methods

---

## Installation

Requires **Python 3.12 or higher**.

```bash
pip install reykit
```

---

# Folders

reykit is organized into multiple folders by functionality, with each folder providing methods and objects for its corresponding functionality.

## `rdll` — DLL file methods

**DLL file methods directory.**

Provides methods for working with Windows system DLL files.

Mainly includes:

* Windows DLL file injection methods
* Other DLL file related methods

---

# Modules

reykit is divided into multiple modules by functionality, with each module providing different general-purpose utilities and base functionality.

## `rall` — All import methods

**Unified export module.**

Provides convenient exports of all reykit module methods and objects. It allows the functionality provided by the package to be imported centrally, reducing the need to import from multiple modules separately.

---

## `rbase` — Base methods

**Base methods module.**

Provides common base methods and shared dependencies used by other modules.

Mainly includes:

* Base classes for various objects
* Exception base classes
* Singleton base classes
* Configuration parameter base classes
* Static metaclasses
* Terminal exit methods
* Exception raising utilities
* Warning raising utilities
* Exception handling utilities
* Exception traceback processing methods
* Value checking methods
* Value type checking methods
* Namespace name processing methods
* Type annotation related methods

---

## `rdata` — Data methods

**Data processing module.**

Provides integrated processing methods for Python basic types and commonly used data.

Mainly includes:

* JWT encoding and decoding
* bcrypt encoding and decoding
* Generator creation utilities
* Array processing methods
* Other data processing methods

---

## `remail` — E-mail methods

**E-mail module.**

Provides integrated methods and objects for e-mail processing.

Mainly includes:

* E-mail content processing
* E-mail property modification
* E-mail sending
* Other e-mail related methods

---

## `rimage` — Image methods

**Image processing module.**

Provides methods for image processing.

Mainly includes:

* Image compression
* QR code encoding
* QR code decoding
* CAPTCHA image generation
* Other image processing methods

---

## `rlog` — Log methods

**Logging module.**

Provides integrated methods and objects for application logging and runtime data storage.

Mainly includes:

* Standard output logging
* Disk file logging
* Log triggering
* Log filtering
* Log processing
* Runtime data storage on disk
* Runtime data saving and checking

---

## `rmonkey` — Monkey patch methods

**Monkey patch module.**

Provides Monkey Patch methods required by other modules.

---

## `rnet` — Network methods

**Network module.**

Provides network-related methods for HTTP, URL, Cookie, Socket, request caching, and more.

Mainly includes:

* Integrated HTTP request methods
* Automatic `Content-Type` handling
* Automatic conversion of Python data types and request bodies
* Automatic response result detection
* Streaming HTTP requests
* URL processing
* Cookie processing
* Socket listening
* Socket data sending
* Global request cache data

---

## `rnum` — Number methods

**Number processing module.**

Provides methods for processing numbers and numeric values.

Mainly includes:

* Base62 conversion
* Chinese number conversion
* Other number processing methods

---

## `ros` — Operation system methods

**Operating system module.**

Provides integrated methods and objects for files, folders, temporary files, and operating system operations.

Mainly includes:

* File and folder operations
* Temporary file and temporary folder operations
* Path processing
* File reading and writing
* File content traversal
* File information retrieval
* File disk storage processing
* Automatic storage directory creation
* File indexing
* File storage
* File deletion
* File comparison

---

## `rrand` — Random methods

**Random value module.**

Provides methods for processing random values and random data.

Mainly includes:

* Global random seed management
* Random indexing
* Random sorting
* Random strings
* Other random value processing methods

---

## `rre` — Regular expression methods

**Regular expression module.**

Provides methods for regular expression processing.

Mainly includes:

* E-mail format validation
* Phone number format validation
* Batch expression matching
* Other regular expression processing methods

---

## `rschedule` — Schedule methods

**Scheduled task module.**

Provides integrated methods and objects for scheduled tasks.

Mainly includes:

* Scheduled task management
* Automatic database storage
* Batch task creation
* Other scheduled task related methods

---

## `rstdout` — Standard output and input methods

**Standard input/output module.**

Provides methods for standard input/output and terminal printing.

Mainly includes:

* Pretty printing of data
* Replacing the global `print` function
* Adding source code locations to global `print` output
* Other standard input/output processing methods

---

## `rsys` — Interpreter system methods

**Interpreter and system module.**

Provides methods related to the Python interpreter and operating system.

Mainly includes:

* Environment variable operations
* Python module table processing
* Terminal command execution
* Process operations
* Memory operations
* Dialog operations
* Other system-related methods

---

## `rtable` — Table methods

**Table processing module.**

Provides integrated table data processing methods and objects.

Supports conversion between different data structures.

Mainly includes:

* Table structure conversion
* Row structure conversion
* JSON conversion
* DataFrame conversion
* HTML text conversion
* CSV conversion
* Excel conversion
* Other table data processing methods

---

## `rtask` — Multi task methods

**Multitasking module.**

Provides integrated methods for threads, coroutines, and multitasking.

Mainly includes:

* Thread pools
* Coroutine pools
* Coroutine launching
* Coroutine integration methods
* Other multitasking methods

---

## `rtext` — Text methods

**Text processing module.**

Provides methods for text and string processing.

Mainly includes:

* Chinese string width processing
* Data-to-text conversion
* Text format beautification
* Chinese character detection
* Other text processing methods

---

## `rtime` — Time methods

**Time processing module.**

Provides methods for time processing and execution time measurement.

Mainly includes:

* Execution time tracking objects
* Execution time calculation
* Execution time reports
* Time object conversion
* Polling and waiting for events to complete
* Other time processing methods

---

## `rwrap` — Decorators

**Decorator module.**

Provides methods for creating decorators and commonly used decorators.

Mainly includes:

* Decorator creation methods
* Decorator enhancement
* Execution time decorators
* Thread execution decorators
* Exception handling decorators
* Cache decorators
* Terminal command argument input decorators
* Print interception decorators
* Other decorator methods

---

# Module Overview

| Module      | Function                                       |
| ----------- | ---------------------------------------------- |
| `rall`      | Unified export of all methods                  |
| `rbase`     | Base methods and shared dependencies           |
| `rdata`     | Python data and basic type processing          |
| `remail`    | E-mail processing                              |
| `rimage`    | Image, QR code, and CAPTCHA processing         |
| `rlog`      | Application logging and runtime data storage   |
| `rmonkey`   | Monkey Patch methods                           |
| `rnet`      | HTTP, URL, Cookie, Socket, and request caching |
| `rnum`      | Number and numeric value processing            |
| `ros`       | File, folder, and operating system processing  |
| `rrand`     | Random value and random data processing        |
| `rre`       | Regular expression processing                  |
| `rschedule` | Scheduled tasks                                |
| `rstdout`   | Standard input/output and terminal printing    |
| `rsys`      | Python interpreter and system operations       |
| `rtable`    | Table data conversion and processing           |
| `rtask`     | Thread, coroutine, and multitasking            |
| `rtext`     | Text and string processing                     |
| `rtime`     | Time and execution time processing             |
| `rwrap`     | Decorator methods                              |

---

# Dependencies

Main dependencies:

* `aiohttp`
* `apscheduler`
* `bcrypt`
* `captcha`
* `concurrent-log-handler`
* `filetype`
* `pandas`
* `pyzbar`
* `pdfplumber`
* `psutil`
* `pymem`
* `python-docx`
* `qrcode`
* `requests`
* `requests_cache`
* `reydb`
* `varname`
* `Pillow`
* `PyJWT`

---

# Project Information

| Project    | Information                                                |
| ---------- | ---------------------------------------------------------- |
| Name       | `reykit`                                                   |
| Version    | `1.2.83`                                                   |
| Python     | `>=3.12`                                                   |
| Author     | `Rey`                                                      |
| Email      | `reyxbo@163.com`                                           |
| Homepage   | [reyxbo.com](https://www.reyxbo.com/release/python/reykit) |
| Repository | [reykit-py](https://github.com/reyxbo/reykit-py.git)       |

## Keywords

`rey` · `reyxbo` · `kit` · `dll` · `email` · `image` · `log` · `net` · `os` · `random` · `regex` · `schedule` · `stdout` · `system` · `table` · `thread` · `async` · `text` · `time` · `decorator`
