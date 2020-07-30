# Notes

## Linux 
  - Linux is a set of operating systems based on the linux kernel. A kernel
  referring to a computer program at the core of a computer's operating system
  with complete control over everything in the system.
  - It free and open source and has many flavours like Debian, Fedora, Ubuntu,
  Mint etc.

## Bash
  - Bash is the command language interpreter/shell (processor), for the GNU
  operating system. The name is an acronym for the ‘Bourne-Again SHell’, a pun
  on Stephen Bourne, who is an English computer scientist.
  - A shell is simply a macro processor that executes commands. A macro is a
  pattern of text that maps to an output sequence of characters

  - Bash is compatible with Bourne Shell sh, Korn shell ksh and the C shell
  csh. It is more interactive and useful for programming than sh, ksh, csh.
  It's also portable and runs on every version of unix there is and also on
  some windows platforms like MS-DOS.

  - Bash can be used to write start up stripts. When Bash starts, it
  executes the commands in a variety of dot files. These startup scripts are
  similar to Bash shell scripts (scripts that have the directive #!/bin/bash
  in them).
  
  - Conditional Execution:
    
  ```sh
    git commit && git push  *(and conditional)*
    git commit || echo "Commit failed"  *(or conditional)*
  ```
  
  - Brace Expansion
    
  ```sh
    {1..5} equivalent to 1 2 3 4 5
  ```
  
  - Variables:
    
  ```
    FILE_NAME="abc"
    echo $FILE_NAME
  ```

## VSCode
  - VSCode is an alternative for sublime.
  - It is a free and open source code editor made by Microsoft. 
  - Features:
    - Debugging
    - Syntax highlighting
    - Code completion
    - Code Snippets
    - Code refactoring
    - Git Version Control (Embedded).
  
## MySQL & SQL
  - MySQL is an open-source Relational Database Management System. A relational
  database is a digital database based on the relational model of data. In
  relational model, data is represented in terms of tuples with each tuple
  representing a relation.
  - The relational data (the tuples) in MySQL are stored in the form of table 
  (each row a tuple).
  - SQL on the other hand, is the used to manipulate data from the relational
  database and also to control user access to the database.
  - MySQL can also be run on cloud computing platforms
  - Some MySQL GUIs are: MySQL Workbench, Adminer, LibreOffice Base, phpMyAdmin
  - Some MySQL CLIs are: 
    - MySQL shell - It supports JavaScript, Python or SQL modes and it can be used for administration and access purposes.
    - Percona Toolkit - A cross-platform toolkit for MySQL, developed in Perl.
  - Many programming languages support libraries for accessing MySQL databases.
  Python, Node.js, C#, Java(JDBC driver) all have such libraries.

## MongoDB
  - MongoDB is a cross-platform document-oriented database program. It is a
  NoSQL database system which stores data in flexible, JSON like documents. In
  a document oriented database program, the data is stored in the form of a
  key-value parirs.
  - Document databases are quite different from relational databases which
  store the data in tables. While a single object can be spread across
  multiple tables in a relational database, document databases store all  
  information for a given object in a single instance in the database.
  - MongoDB supports field, range query, and regular-expression searches.
  - Fields in a MongoDB document can be indexed with primary and secondary indices.
  - MongoDB can prevent hardware failure disruptions when run over multiple
  servers. It does data duplication to keep the system up and running in case
  of hardware failure.

## Elasticsearch
  - Elasticsearch is a search engine based on the Lucene library. Lucene 
  (Apache Lucene) is a free, open-source seach engine software library. Lucene
  has been used in the implementation of Internet search engines and local,
  single-site searching.
  - It provides a distributed full-text search engine with an HTTP web interface and schema-free JSON documents
  - Elastic Stack (ELK Stack) for log and metric analytics:
    - A collection of lightweight data shippers (agents installed on edge hosts
    to collect different types of data) called Beats. 
    - A data collection and log-parsing engine called Logstash (collects data from various input sources, executes different transformations and enhancements and then ships the data to various supported output destinations)
    - An analytics and visualisation platform called Kibana (visualization layer)
    - Elasticsearch (the search engine that indexes and stores the data)

## Redis
  - Redis is an open source, in-memory data structure store
  - Its used as a database, caching system.
  - All Redis data resides in-memory, in contrast to databases that store data on disk or SSDs. By eliminating the need to access disks, in-memory data stores such as Redis avoid seek time delays and can access data in microseconds.
  - It supports data structures such as strings, hashes, lists, sets, bitmaps.
  - You can run atomic operations like appending to a string; incrementing the
  value in a hash; pushing an element to a list; computing set intersection,
  union and difference; or getting the member with highest ranking in a sorted
  set on redis.
  - Redis makes it simpler to build real-time internet scale apps.

## Pandas
  - Pandas is an easy to use open source data analysis and manipulation tool,
  built on top of the Python programming language. The name is derived from the term "panel data".
  - It offers data structures and operations for manipulating numerical tables
  and time series
  - Features: DataFrames, Data reading and writing, Insertion and deletion etc.

## Flask
  - Flask is a python framework. A framework is a code library that makes it
  easier for a developer when he/she is building reliable, scalable, and
  maintainable web applications. A framework does this by providing reusable
  code or extensions for common operations.
  - The main feature of flask is that it's a micro framework. The word “micro”
  in micro framework means Flask aims to keep the core simple but extensible.
  Micro frameworks are normally frameworks with little to no dependencies to
  external libraries
  - Dependensies of flask: Werkzeug, Jinja2
  - Flask is considered more Pythonic than the Django web framework because in common situations the equivalent Flask web application is more explicit.
  - Flask is also easy to get started with as a beginner because there is
  little required code for getting a simple app up and running.

## Tornado
  - Tornado is a web python framework but it is built specifically to handle
  asynchronous processes.
  - Tornado doesn't require any external configuration, we can dive right into
  writing the Python code that'll run our application.
  - By using non-blocking network I/O, Tornado can scale to tens of thousands
  of open connections, making it ideal for applications that require a
  long-lived connection to each user (real-time web features sometimes require
  a long-lived mostly-idle connection per user).
  - The Tornado web framework and HTTP server together offer a full-stack
  alternative to WSGI (Python Web Server Gateway Interface).


## GCP
  - Google Cloud Platform (GCP) is a suite of cloud computing services offered
  by Google.
  - Some of the products offered are: Kubernetes Engine, App Engine, Compute
  Engine, Cloud Function, Cloud Run, Cloud Storage, Cloud SQL, Persistent Disk,
  Local SSD, Filestore, Cloud DNS etc.

## Git & Github
  - Git is a version control software and Github is an online platform
  providing git features for software.
